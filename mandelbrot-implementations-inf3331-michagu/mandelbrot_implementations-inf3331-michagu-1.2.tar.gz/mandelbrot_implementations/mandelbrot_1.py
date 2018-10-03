import numpy as np

# Have to handle imports differently from when running the test from outside the package and from within.
if __name__ == "mandelbrot_implementations.mandelbrot_1":
    import mandelbrot_implementations.constant as constants
else:
    import constant as constants

def mandelbrot_pure_python(z):
    """ Regner ut escape time for det gitte komplekse tallet.

    :param z: Det komplekse tallet.
    :return: Escape time for det komplekse tallet, 0 om det er i settet, antall iterasjoner for å få det over limit ellers.
    """
    c = z
    for n in range(constants.MAX_ITERASJONER):
        if abs(z) > 2:
            return n + 1
        z = z * z + c
    return 0


def mandelbrot_set(xmin, xmax, ymin, ymax, nX, nY):
    """ Opprett punkter/arrays og kall på "mandelbrot utregningen" for hvert punkt.

    :param xmin: Min value for x-aksen
    :param xmax: Max value for x-aksen
    :param ymin: Min value for y/imaginære aksen
    :param ymax: Max value for y/imaginære aksen
    :param nX: Antall punkter for x-aksen
    :param nY: Antall punkter for y-aksen
    :return: Et array med beregnet escape times
    """
    x_aksen = np.linspace(xmin, xmax, nX)  # Numpy array for x-aksen med gitt "resolution"
    y_aksen = np.linspace(ymin, ymax, nY)  # Numpy array for y-aksen med gitt "resolution"
    escape_times = np.empty((nX, nY))      # 2D Numpy array for escape times
    for i in range(nX):
        for j in range(nY):
            escape_times[i, j] = mandelbrot_pure_python(complex(x_aksen[i], y_aksen[j]))
    return escape_times
