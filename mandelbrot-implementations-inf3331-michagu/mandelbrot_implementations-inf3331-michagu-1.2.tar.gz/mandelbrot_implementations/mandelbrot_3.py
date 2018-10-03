import numpy as np
from numba import jit
if __name__ == "mandelbrot_implementations.mandelbrot_3":
    import mandelbrot_implementations.constant as constants
else:
    import constant as constants


@jit(nopython=True)
def mandelbrot_numba(z):
    c = z
    for n in range(constants.MAX_ITERASJONER):
        if abs(z) > 2:
            return n + 1
        z = z * z + c
    return 0


@jit(nopython=True)
def mandelbrot_set(xmin, xmax, ymin, ymax, nX, nY):
    """Opprett punkter/arrays og kall på "mandelbrot utregningen" for hvert punkt.

    :param xmin: Min value for x-aksen
    :param xmax: Max value for x-aksen
    :param ymin: Min value for y/imaginære aksen
    :param ymax: Max value for y/imaginære aksen
    :param nX: Antall punkter for x-aksen
    :param nY: Antall punkter for y-aksen
    :return: Et array med beregnet escape times
    """
    x_range = np.linspace(xmin, xmax, nX)
    y_range = np.linspace(ymin, ymax, nY)
    res = np.empty((nX, nY))
    for j in range(nX):
        for i in range(nY):
            res[i, j] = mandelbrot_numba(complex(x_range[i], y_range[j]))
    return res
