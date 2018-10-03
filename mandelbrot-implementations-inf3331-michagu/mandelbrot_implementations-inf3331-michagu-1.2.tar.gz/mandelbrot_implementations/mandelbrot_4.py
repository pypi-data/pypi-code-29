"""
Jeg bruker pyximport, da man slipper å kjøre setup.py for
hver gang man endrer på koden i mandelbrot_cython.pyx. pyximport kan
brukes så lenge man ikke bruker noen ekstra c-biblioteker eller
har en spesiell bygg-setup. Det som pyximport gjør er å kalle
Cython på hver .pyx vi importerer under.
"""
import pyximport; pyximport.install()
if __name__ == "mandelbrot_implementations.mandelbrot_4":
    import mandelbrot_implementations.constant as constants
    from mandelbrot_implementations.mandelbrot_cython import mandelbrot_set
else:
    import constant as constants
    from mandelbrot_cython import mandelbrot_set


def mandel_med_cython(xmin, xmax, ymin, ymax, nX, nY):
    z = mandelbrot_set(xmin, xmax, ymin, ymax, nX, nY, constants.MAX_ITERASJONER)
    return z
