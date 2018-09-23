'''pol2cart function definition'''

import numpy


def pol2cart(r, theta, pol, pxo, pyo, xmin, xmax, ymin, ymax,
             xstep=None, ystep=None):

    '''
    Utility function to convert polar to Cartesian data.

    For each Cartesian coordinate, the assigned value is linearly interpolated
    from the values at the four encompassing polar coordinates.

    The input polar grid is assumed to be uniformly spaced in both radial and
    angle coordinates. The Cartesian grid uses a right hand up frame. Polar
    angles are defined as clockwise positive between 0 and 2*pi relative to the
    y axis (i.e. the angle is zero for positive y with x=0). Alternatively they
    can be defined between -pi and pi.

    The input grid can be 2D (theta, r) or 3D (N, theta, r). For 3D data the
    interpolation described above is applied over all N points.
    -------
    args...
    -------
    r: polar radial coordinate (numpy array)
    theta: polar angle coordinate in radians (numpy array)
    pol: polar data (numpy ndarray, dimensions theta.size,r.size for 2D data
         or N,theta.size,r.size for 3D data)
    pxo, pyo: origin of polar data in Cartesian frame
    xmin, xmax: x coordinate bounds of interpolated Cartesian data
    ymin, ymax: y coordinate bounds of interpolated Cartesian data
    ---------
    kwargs...
    ---------
    xstep, ystep: x and y interpolation intervals (both default to r interval)
    ----------
    returns...
    ----------
    x: Cartesian x coordinate (numpy array)
    y: Cartesian y coordinate (numpy array)
    cart: Interpolated Cartesian data (numpy array, dimensions x.size,y.size
          for 2D data or N,x.size,y.size for 3D data)
    '''

    # Check the dimensions

    nr = r.size
    ntheta = theta.size

    dims = pol.shape
    is3d = False
    if len(dims) == 3:
        is3d = True
        nz = dims[0]
        check_dims = dims[1:]
    else:
        check_dims = dims

    if (ntheta, nr) != check_dims:
        raise ValueError('Input dimensions are not consistent')

    # Check theta range

    tpos = True
    if theta[0] < 0:
        if theta[-1] > 180:
            raise ValueError('Input polar angles must range between 0 and 2*pi or -pi and pi')
        else:
            tpos = False

    dtheta = theta[1] - theta[0]
    dr = r[1] - r[0]

    # Check if wrapping round possible

    wrap_ok = False
    if tpos:
        if (theta[0] <= dtheta / 2) and (theta[-1] + dtheta >= 2 * numpy.pi):
            wrap_ok = True
    elif (theta[0] - dtheta / 2 <= -numpy.pi) and (theta[-1] + dtheta >= numpy.pi):
        wrap_ok = True

    # Set up arrays

    if xstep is None:
        xstep = dr
    if ystep is None:
        ystep = dr

    nx = int(numpy.round((xmax - xmin) / xstep)) + 1
    ny = int(numpy.round((ymax - ymin) / ystep)) + 1
    x = numpy.linspace(xmin, xmax, nx)
    y = numpy.linspace(ymin, ymax, ny)

    if is3d:
        cart = numpy.ones([nz, nx, ny]) * numpy.nan
    else:
        cart = numpy.ones([nx, ny]) * numpy.nan

    # Interpolate

    for xn in range(nx):

        xc = x[0] + xn * xstep - pxo

        for yn in range(ny):

            yc = y[0] + yn * ystep - pyo

            int_ok = True

            thetac = numpy.arctan2(xc, yc)
            if tpos and (thetac < 0):
                thetac += 2 * numpy.pi

            if (thetac < theta[0]) or (thetac > theta[-1] + dtheta):
                int_ok = False

            theta_ind0 = int(numpy.floor((thetac - theta[0]) / dtheta))
            theta_ind1 = theta_ind0 + 1

            if theta_ind1 >= ntheta:
                if wrap_ok:  # Wrap around to zero
                    theta_ind0 = ntheta - 1
                    theta_ind1 = 0
                else:
                    int_ok = False

            if int_ok:
                rc = numpy.sqrt(xc**2 + yc**2)
                r_ind = int(numpy.floor((rc - r[0]) / dr))

            if int_ok and (0 <= r_ind < nr):

                # r interpolation

                if r_ind < nr - 1:
                    interp_r = True
                else:
                    interp_r = False

                if is3d:
                    pol00 = pol[:, theta_ind0, r_ind]
                    pol10 = pol[:, theta_ind1, r_ind]
                    if interp_r:
                        pol01 = pol[:, theta_ind0, r_ind + 1]
                        pol11 = pol[:, theta_ind1, r_ind + 1]
                else:
                    pol00 = pol[theta_ind0, r_ind]
                    pol10 = pol[theta_ind1, r_ind]
                    if interp_r:
                        pol01 = pol[theta_ind0, r_ind + 1]
                        pol11 = pol[theta_ind1, r_ind + 1]

                if interp_r:
                    pol0 = pol00 + (rc - r[r_ind]) * (pol01 - pol00) / dr
                    pol1 = pol10 + (rc - r[r_ind]) * (pol11 - pol10) / dr
                else:
                    pol0 = pol00
                    pol1 = pol10

                # theta interpolation

                poli = pol0 + (thetac - theta[theta_ind0]) * (pol1 - pol0) / dtheta

                if is3d:
                    cart[:, xn, yn] = poli
                else:
                    cart[xn, yn] = poli

    return x, y, cart
