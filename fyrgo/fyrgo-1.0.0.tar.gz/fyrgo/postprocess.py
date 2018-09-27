"""Some postprocessing functions."""
import itertools as itt

import numpy as np

from fyrgo import DataLoader

_directions = {k:0 for k in ['theta','phi','angle','angular','azim','azimuthal']}
_directions.update({k:1 for k in ['r','rad','radial','radius']})


def profile(array, direction='azimuthal'):
    '''Get the 1D version of an array averaged over a given direction.'''
    if direction in _directions.keys():
        ax = _directions[direction]
    elif isinstance(direction, int):
        ax = direction
    return array.mean(axis=ax)


def crop(x:np.ndarray, y:np.ndarray, z:np.ndarray,
         xmin:float=None, xmax:float=None,
         ymin:float=None, ymax:float=None
) -> tuple:
    '''Exctract a region of (x,y) meshgrid and z data (2D arrays)
    according to specified limits.
    '''
    assert x.shape == y.shape == z.shape
    x1 = xmin or np.min(x)
    x2 = xmax or np.max(x)
    y1 = ymin or np.min(y)
    y2 = ymax or np.max(y)
    r, c = np.where((x > x1) & (x < x2) & (y > y1) & (y < y2))
    a, b = max(r)-min(r)+1, max(c)-min(c)+1
    return tuple([d[r,c].reshape(a,b) for d in (x,y,z)])


def write_a_fargo_binary(array:np.ndarray, key:str, offset:int, directory:str, verbose=False):
    '''A simple writter to emulate fargo data files for fields.

    This can be used to generate arbitrary initial conditions files.
    array is assumed to be of same shape as a DataLoader.fields[key]
    '''
    a,b = array.shape
    file_name = str(directory) + f'/gas{key}{offset}.dat'
    mess = f'Error while writting {file_name}'
    try:
        with open(file_name, 'wb') as f:
            array.T.reshape(a*b).tofile(f)
            mess = f'Successfully wrote {file_name}'
    finally:
        print(mess)


def torque_from_density(dl:DataLoader, offset:int, x:float, y:float, G_grav:float=1.0) ->np.array:
    '''Compute the radial (specific) torque profile acting on an arbitrary point of the grid (x,y).

    This is based on internal computations of FARGO, regarding the
    force the disk exerts on a planet.
    '''
    # devnotes
    # --------
    #  * no option for smoothing yet
    #  * a minus sign is applied at the end to reproduce FARGO's output,
    #    but maybe I left a sign error somewhere and this is in fact not a matter of convention here
    #  * user should be able to use polar coordinates instead of cartesian ones
    #  * it would be easy to optionnally return a 2D array
    #  * when this is fully tested, fargOCA could be simplified (stop priting 1D torque profiles)
    assert(offset in dl.offsets and dl.is_loaded),\
        f"DataLoader object must contain required offset ({offset})"

    rmed,theta = np.meshgrid(dl['rmed'], dl['theta'])
    X_cells = rmed*np.cos(theta)
    Y_cells = rmed*np.sin(theta)
    force_x = np.zeros(dl['nrad'])
    force_y = np.zeros(dl['nrad'])
    torque  = np.zeros(dl['nrad'])
    for i,j in itt.product(range(dl['nrad']), range(dl['nsec'])):
        xc = X_cells[j,i]
        yc = Y_cells[j,i]
        mc = dl['surf'][i] * dl['dens'][offset][j,i] #cell mass
        dx,dy = x-xc, y-yc
        d = np.sqrt(dx**2+dy**2)
        potc = - G_grav*mc/d
        force_x[i] += - potc/d**2 *dx #this is an acceleration (same notations as FARGO)
        force_y[i] += - potc/d**2 *dy
    for i in range(dl['nrad']):
        torque = -(x*force_y - y*force_x)
    return torque
