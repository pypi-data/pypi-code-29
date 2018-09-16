"""steepest.py - A Steepest Ascent (Descent) segmentation algorithm

This module implements a watershed algorithm that apportions pixels into
marked basins. The algorithm uses a priority queue to hold the pixels
with the metric for the priority queue being pixel value, then the time
of entry into the queue - this settles ties in favor of the closest marker.

Some ideas taken from
Soille, "Automated Basin Delineation from Digital Elevation Models Using
Mathematical Morphology", Signal Processing 20 (1990) 171-182.

The most important insight in the paper is that entry time onto the queue
solves two problems: a pixel should be assigned to the neighbor with the
largest gradient or, if there is no gradient, pixels on a plateau should
be split between markers on opposite sides.

Originally part of CellProfiler, code licensed under both GPL and BSD licenses.
Website: http://www.cellprofiler.org

Copyright (c) 2003-2009 Massachusetts Institute of Technology
Copyright (c) 2009-2011 Broad Institute
All rights reserved.

Original author: Lee Kamentsky
"""

import numpy as np
from scipy import ndimage as ndi
import networkx as nx
import mahotas as mh
import skimage
import tifffile as tiff
import scipy
from pycostanza.misc import crop


def _validate_inputs(image, mask, resolution):
    """Ensure that all inputs to segmentation have matching shapes and types.
    Modified from the Scikit-Image watershed code.

    Parameters
    ----------
    image : array
        The input image.
    mask : array, or None
        A boolean mask, True where we want to segment.
    resolution : array, or None
        Resolution per dimension of the input image.

    Returns
    -------
    image, mask, resolution: arrays
        The validated and formatted arrays. Image will have dtype float64,
        and mask int8. If ``None`` was given for the mask,
        it is a volume of all 1s.

    Raises
    ------
    ValueError
        If the shapes of the given arrays don't match.
    """
    if not isinstance(image, np.ndarray):
        image = np.array(image)
    if not isinstance(mask, np.ndarray):
        mask = np.array(mask)
    if not isinstance(resolution, np.ndarray):
        resolution = np.array(resolution)

    if mask is not None and mask.shape != image.shape:
        raise ValueError("`mask` must have same shape as `image`")
    if mask is None:
        # Use a complete `True` mask if none is provided
        mask = np.ones(image.shape, bool)
    if resolution is None:
        resolution = np.ones((image.ndim), np.float64)
    elif len(resolution) != image.ndim:
        raise ValueError(
            "`resoltion` must have a value per dimension of `image`")

    return (image.astype(np.float64),
            mask.astype(np.int8),
            resolution.astype(np.float64))


def _validate_connectivity(image_dim, connectivity, offset):
    """Convert any valid connectivity to a structuring element and offset.

    Parameters
    ----------
    image_dim : int
        The number of dimensions of the input image.
    connectivity : int, array, or None
        The neighbourhood connectivity. An integer is interpreted as in
        ``scipy.ndimage.generate_binary_structure``, as the maximum number
        of orthogonal steps to reach a neighbor. An array is directly
        interpreted as a structuring element and its shape is validated against
        the input image shape. ``None`` is interpreted as a connectivity of 1.
    offset : tuple of int, or None
        The coordinates of the center of the structuring element.

    Returns
    -------
    c_connectivity : array of bool
        The structuring element corresponding to the input `connectivity`.
    offset : array of int
        The offset corresponding to the center of the structuring element.

    Raises
    ------
    ValueError:
        If the image dimension and the connectivity or offset dimensions don't
        match.
    """
    if connectivity is None:
        connectivity = 1

    if np.isscalar(connectivity):
        c_connectivity = ndi.generate_binary_structure(image_dim, connectivity)
    else:
        c_connectivity = np.array(connectivity, bool)
        if c_connectivity.ndim != image_dim:
            raise ValueError("Connectivity dimension must be same as image")

    if offset is None:
        if any([x % 2 == 0 for x in c_connectivity.shape]):
            raise ValueError("Connectivity array must have an unambiguous "
                             "center")

        offset = np.array(c_connectivity.shape) // 2

    return c_connectivity, offset


def _compute_neighbours(image, structure, offset):
    """Compute neighbourhood as an array of linear offsets into the image.

    These are sorted according to Euclidean distance from the center (given
    by `offset`), ensuring that immediate neighbours are visited first.
    """
    structure[tuple(offset)] = 0  # ignore the center; it's not a neighbor
    locations = np.transpose(np.nonzero(structure))
    sqdistances = np.sum((locations - offset)**2, axis=1)
    neighbourhood = (np.ravel_multi_index(locations.T, image.shape) -
                     np.ravel_multi_index(offset, image.shape))
    sorted_neighbourhood = neighbourhood[np.argsort(sqdistances)]
    return sorted_neighbourhood


def get_footprint(dimensions, connectivity, offset=None):
    return _validate_connectivity(dimensions, connectivity, offset)[0]


def steepest_ascent(image, resolution=None, connectivity=1, offset=None, mask=None):
    """Find attractor basins in `image` based on a steepest ascent approach of
    the input image,

    Parameters
    ----------
    image: ndarray (2-D, 3-D, ...) of integers
        Raw intensity array.
    connectivity: ndarray, optional
        An array with the same number of dimensions as `image` whose
        non-zero elements indicate neighbours for connection.
        Following the scipy convention, default is a one-connected array of
        the dimension of the image.
    offset: array_like of shape image.ndim, optional
        offset of the connectivity (one offset per dimension)
    mask: ndarray of bools or 0s and 1s, optional
        Array of same shape as `image`. Only points at which mask == True
        will be labeled.

    Returns
    -------
    out: ndarray
        A labeled matrix denoting the different attractor basins in the input.

    """

    image, mask, resolution = _validate_inputs(image, mask, resolution)
    connectivity, offset = _validate_connectivity(image.ndim, connectivity,
                                                  offset)

    # get the distances to the neighbours
    neighbours = connectivity.copy()
    neighbours[tuple(offset)] = False
    neighbours = np.array(np.where(neighbours)).T
    neighbours = np.multiply(neighbours, resolution)
    neighbours = np.subtract(neighbours, offset)

    distances = np.linalg.norm(neighbours, axis=1)

    # pad the image, and mask so that we can use the mask to keep from running
    # off the edges
    pad_width = [(p, p) for p in offset]
    image = np.pad(image, pad_width, mode='constant')
    mask = np.pad(mask, pad_width, mode='constant')
    output = np.zeros(image.shape, dtype=np.uint16)

    # get flattened versions of everything
    flat_neighbourhood = _compute_neighbours(image, connectivity, offset)
    image_raveled = image.ravel()
    indices = np.where(mask.ravel())[0]

    # compute forward gradients in all directions, and couple the cell with the
    # neighbour to which the gradient is the steepest
    # TODO - BUG: Avoid doing this for the attractors, as it will couple to the neighbour with the smallest slope.
    point_neighbours = np.array(map(lambda x: x + flat_neighbourhood, indices))
    fw_gradients = np.subtract(image_raveled[point_neighbours].T,
                               image_raveled[indices]).T / distances

    steepest_neighbours = np.argmax(fw_gradients, axis=1)
    connections = point_neighbours[xrange(
        point_neighbours.shape[0]), steepest_neighbours]

    # Reduce to the connected components
    graph = nx.Graph()
    graph.add_edges_from(zip(indices, connections))
    components = nx.connected_components(graph)

    # Label
    output_raveled = output.ravel()
    for label, members in enumerate(components, start=1):
        output_raveled[np.array(list(members))] = label

    output = crop(output, pad_width, copy=False)

    return output

