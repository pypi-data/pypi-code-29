from setuptools import setup


setup(
    name='mandelbrot_implementations-inf3331-michagu',
    version='1.02',
    packages=['mandelbrot_implementations'],
    url='https://github.com/UiO-INF3331/INF3331-michagu/tree/master/assignment4/mandelbrot_implementations',
    license='',
    keywords='inf3331 mandelbrot_implementations fractal',
    author='theagilepadawan',
    author_email='michagu@ifi.uio.no',
    description='Various implementations computing and drawing the mandelbrot_implementations set',
    install_requires=[
        'matplotlib',
        'numpy',
        'argparse',
        'cython',
        'numba'
    ],
    include_package_data=True,
)

