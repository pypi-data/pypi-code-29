"""
Jeg bruker argparser som er en del Python sitt standard
bibliotek og som da er en command line parser.
Hvorfor finne opp hjulet på nytt? :)
"""
import argparse
import matplotlib.pyplot as plt
from matplotlib import colors
if __name__ == "__main__":
    import mandelbrot_1 as mb1
    import mandelbrot_2 as mb2
    import mandelbrot_3 as mb3
    import mandelbrot_4 as mb4
    import constant as constants
else:
    from mandelbrot_implementations import mandelbrot_1 as mb1
    from mandelbrot_implementations import mandelbrot_2 as mb2
    from mandelbrot_implementations import mandelbrot_3 as mb3
    from mandelbrot_implementations import mandelbrot_4 as mb4
    from mandelbrot_implementations import constant as constants


parser = argparse.ArgumentParser()
dpi = 72
# Da Python ikke har case/switch statement kan man løse det med en dictionary
implementasjoner = {
    1: mb1.mandelbrot_set,
    2: mb2.mandelbrot_set,
    3: mb3.mandelbrot_set,
    4: mb4.mandel_med_cython
}
color_scales = {
    1: "jet_r",
    2: "magma",
    3: "gnuplot2"
}


def mandelbrot_image(res, filname, xmin, xmax, ymin, ymax, nX, nY, cmap_inn="jet_r"):
    """ Tegn bildet gitt det arrayet med escape times.

    :param res: Arrayet med escape times
    :param filname: Filnavn for bildet som genereres.
    :param xmin: Min value for x-aksen
    :param xmax: Max value for x-aksen
    :param ymin: Min value for y/imaginære aksen
    :param ymax: Max value for y/imaginære aksen
    :param nX: Antall punkter for x-aksen
    :param nY: Antall punkter for y-aksen
    :param cmap_inn: Valgt color map, default er jet_r
    """
    fig, ax = plt.subplots(figsize=((nX / dpi), (nY / dpi)), dpi=dpi)
    cmap = plt.get_cmap(cmap_inn)
    cmap.set_under("black") # At verdi 0 faktisk blir sort
    gamma = 0.67
    norm = colors.PowerNorm(gamma)
    plt.title(f"Escape time:{constants.MAX_ITERASJONER} | x: {xmin} - {xmax} y: {ymin} - {ymax} | {nX}x{nY} | Colormap: {cmap.name}")
    ax.imshow(res.T, cmap=cmap, norm=norm)
    plt.savefig(str(filname))


def parser_builder(*arg, **kwargs):
    """ For å kunne chaine argumenter som legges til,
    og fungerer da som en builder. Kun for en egen fornøyelse :)

    :param arg: Selve argumentet til argparseren
    :param kwargs: Eventuelle keyword arguments.
    :return: metode-objektet slik at jeg kan bruke det som en builder
    """
    parser.add_argument(*arg, **kwargs)
    return parser_builder


def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None):
    """

    :param xmin: Min value for x-aksen
    :param xmax: Max value for x-aksen
    :param ymin: Min value for y/imaginære aksen
    :param ymax: Max value for y/imaginære aksen
    :param nX: Antall punkter for x-aksen
    :param nY: Antall punkter for y-aksen
    :param max_escape_time: Hvor mange ganger funksjonen anvendes før vi konkluderer med at tallet er i settet.
    :param plot_filename: Filnavn om man ønsker at bildet skal tegnes og lagres.
    :return: Nx x Ny array med escape times
    """
    constants.MAX_ITERASJONER = max_escape_time
    res = mb2.mandelbrot_set(xmin, xmax, ymin, ymax, Nx, Ny)
    if res.all() == 1:
        print("We're entirely outside the Mandelbrot set after 0 iterations, canceling drawing")
        return None
    if plot_filename is not None:
        mandelbrot_image(res, plot_filename, xmin, xmax, ymin, ymax, Nx, Ny)
    return res


if __name__ == '__main__':
    parser_builder("minX", help="Min value for x-axes", type=float)\
                  ("maxX", help="Max value for x-axes", type=float)\
                  ("minY", help="Min value for y-axes", type=float)\
                  ("maxY", help="Max value for y-axes", type=float)\
                  ("nX", help="Resolution for the x-axes", type=int)\
                  ("nY", help="Resolution for the  y-axes", type=int)\
                  ("filename", help="Filename for the Mandelbrot set")\
                  ("-m", "--mandelbrot_implementation", help="1.Pure Python | 2.Numpy | 3.Numba | 4.Cython - defaults to Cython", default=4, type=int)\
                  ("-c", "--color_scale", help="1.jet_r | 2.magma | 3.gnuplot2 - defaults to jet_r", default=1, type=int)\
                  ("-t", "--max_escape_time", help="Max escape time, defaults to 1000", default=1000, type=int)
    args = parser.parse_args()

    if args.mandelbrot_implementation > 4 or args.mandelbrot_implementation < 1:
        parser.error("Invalid number for implementation")

    if args.max_escape_time < 50:
        parser.error("Lower limit: 50 for escape time")

    if args.color_scale > 3 or args.color_scale < 1:
        parser.error("Invalid number for color scale")

    constants.MAX_ITERASJONER = args.max_escape_time
    valgt_implementasjon = implementasjoner.get(args.mandelbrot_implementation)
    cmap = color_scales.get(args.color_scale)
    res = valgt_implementasjon(args.minX, args.maxX, args.minY, args.maxY, args.nX, args.nY)
    # if res.all() == 1:
    #     print("We entirely outside the Mandelbrot set after 0 iterations, canceling drawing")
    #     exit()
    mandelbrot_image(res, args.filename, args.minX, args.maxX, args.minY, args.maxY, args.nX, args.nY, cmap)
