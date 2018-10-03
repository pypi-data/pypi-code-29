import numpy as np

# Have to handle imports differently from when running the test from outside the package and from within
if __name__ == "mandelbrot_implementations.mandelbrot_2":
    import mandelbrot_implementations.constant as constants
else:
    import constant as constants


def mandelbrot_med_numpy(c):
    """Beregner mandelbrotsettet ved hjelp av numpy arrays

    Tar inn numpy array med komplekse tallene i det utvalgte rektangelet
    og beregner hvilke av tallene som ligger i mandelbrottsettet, samt de hvor
    mange ganger vi har måtte kalle på funksjonen for at de andre tallene kom utenfor
    planet.


    :param c: Numpy arrayet med de komplekse tallene.
    :return: Numpy array med verdier, hvor 0 vil si at tallet er med i settet.
    """
    res = np.zeros(c.shape)                                     # oppretter et numpy array for resultatene
    z = np.zeros(c.shape, np.complex64)                         # dette skal være et numpy array med komplekse tall
    for it in range(constants.MAX_ITERASJONER):
        notdone = np.less(z.real*z.real + z.imag*z.imag, 4.0)   # returnerer et array med bools (om punktet er over 2)
        res[notdone] = it + 1                                   # inkrementer plassen til tallene som ikke er gått over (antall ganger funksjonen er kalt)
        z[notdone] = z[notdone]**2 + c[notdone]                 # i.e x^2 +c (mandelbrot_implementations-funksjonen)
    res[res == constants.MAX_ITERASJONER] = 0                   # sett alle tall (plasser i arrayet) som er med i settet til 0
    return res


def mandelbrot_set(xmin,xmax,ymin,ymax, nX, nY):
    """ Oppretter numpy arrays og kaller på selve utregningen av mandelbrottsettet

    :param xmin: Min value for x-aksen
    :param xmax: Max value for x-aksen
    :param ymin: Min value for y/imaginære aksen
    :param ymax: Max value for y/imaginære aksen
    :param nX: Antall punkter for x-aksen
    :param nY: Antall punkter for y-aksen
    :return: Numpy array med verdier som brukes for å fargelegge senere. 0 betyr at tallet er i settet,
             alle tall over null er hvor mange ganger funksjonen vi måtte anvende funksjonen for at tallet gikk over 2.
    """
    x_range = np.linspace(xmin, xmax, nX)  # Opprett array for x-aksen
    y_range = np.linspace(ymin, ymax, nY)  # Opprett array for y-aksen/ imaginære aksen
    y_range = y_range[:, None]*1j          # Utvid arrayet til å kunne holde komplekse tallene
    complex_nums = x_range + y_range       # Opprett nytt array med de komplekse tallene til rektangelet i det komplekse "rommet"
    n3 = mandelbrot_med_numpy(complex_nums)
    return n3.T