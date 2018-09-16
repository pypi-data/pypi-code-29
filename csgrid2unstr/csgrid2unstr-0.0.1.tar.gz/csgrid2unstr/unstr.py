"""Unstructurize module

This module is to convert CSGrid object into an unstructure mesh that contains
a coordinate table and a connectivity table. Notice that the orientation of
quadrilateral cells follows the right-hand rule thus having outward normals.

.. moduleauthor:: Qiao Chen <benechiao@gmail.com>
"""

import numpy as np


class Unstr(object):
    """Unstructurize CSGrid

    Parameters
    ----------
    csgrid : :py:class:`~csgrid2unstr.cubed_sphere.CSGrid`
        cubed-sphere grid

    Attributes
    ----------
    points : np.ndarray
        points stored in (nx3)
    cells : np.ndarray
        connectivity table stored in (mx4)
    """

    def __init__(self, csgrid):
        self._cs = csgrid

        self.points, self.cells = self._build()

    def _build(self):
        # build tables
        f2n, nids, N = self._build_tables()

        cs = self._cs
        c = cs.c
        cc = c**2

        # allocate memory for cells, points, and centroids
        points = np.empty((N, 3))
        cells = np.empty((6*cc, 4), dtype=int)

        p_counter = 0

        for face in range(6):
            xyz = cs.xyz_edge[:, :, :, face]
            local = np.asarray([0, 1, c+2, c+1])
            fs = f2n[face]
            nid = nids[face]
            cell_start = face*cc
            for cell in range(cc):
                cells[cell+cell_start] = fs.flat[local]
                local += 1 + ((cell+1) % c == 0)
            if not nid:
                continue
            for x in nid[0]:
                for y in nid[1]:
                    points[p_counter] = xyz[:, x, y]
                    p_counter += 1

        return points, cells

    def _build_tables(self):
        cs = self._cs
        n = cs.nx
        nn = n-2
        f2n = np.empty((6, n, n), dtype=int)
        nids = []

        counter = 0

        # face 1
        f2n[0][:] = np.arange(0, n*n, dtype=int).reshape(n, n)
        counter += n*n
        nids.append([])
        nids[-1].append(np.arange(n, dtype=int))
        nids[-1].append(nids[-1][0])

        # face 2
        f2n[1][0] = f2n[0][-1]
        f2n[1][1:] = np.arange(counter, counter+(n-1)*n,
                               dtype=int).reshape(n-1, n)
        counter += (n-1)*n
        nids.append([])
        nids[-1].append(nids[0][0][1:])
        nids[-1].append(nids[0][0])

        # face 3
        f2n[2][0] = f2n[0][:, 0]
        f2n[2][:, -1] = f2n[1][:, 0]
        f2n[2][1:n, :n-1] = np.arange(counter, counter +
                                      (n-1)*(n-1), dtype=int).reshape(n-1, n-1)
        counter += (n-1)*(n-1)
        nids.append([])
        nids[-1].append(nids[0][0][1:])
        nids[-1].append(nids[0][0][:n-1])

        # face 4
        f2n[3][0] = f2n[2][-1]
        f2n[3][:, -1] = f2n[1][-1]
        f2n[3][1:n, :n-1] = np.arange(counter, counter +
                                      (n-1)*(n-1), dtype=int).reshape(n-1, n-1)
        counter += (n-1)*(n-1)
        nids.append([])
        nids[-1].append(nids[0][0][1:])
        nids[-1].append(nids[0][0][:n-1])

        # face 5
        f2n[4][0] = f2n[2][:, 0]
        f2n[4][:, 0] = f2n[0][0]
        f2n[4][:, -1] = f2n[3][:, 0]
        nids.append([])
        if nn:
            f2n[4][1:n, 1:n-1] = np.arange(
                counter,
                counter+nn*(n-1),
                dtype=int
            ).reshape(n-1, nn)
            counter += nn*(n-1)
            nids[-1].append(nids[0][0][1:])
            nids[-1].append(nids[0][0][1:n-1])

        # face 6
        f2n[5][0] = f2n[4][-1]
        f2n[5][:, 0] = f2n[0][:, -1]
        f2n[5][:, -1] = f2n[3][-1]
        f2n[5][-1] = f2n[1][:, -1]
        nids.append([])
        if nn:
            f2n[5][1:n-1, 1:n-1] = np.arange(
                counter,
                counter+nn*nn,
                dtype=int
            ).reshape(nn, nn)
            counter += nn*nn
            nids[-1].append(nids[0][0][1:n-1])
            nids[-1].append(nids[0][0][1:n-1])

        return f2n, nids, counter
