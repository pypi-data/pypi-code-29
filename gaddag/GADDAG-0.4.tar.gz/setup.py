from setuptools import setup, Extension
from distutils.command.build_ext import build_ext


class build_ext(build_ext):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypes)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + '.so'
        return super().get_ext_filename(ext_name)


class CTypes(Extension):
    pass


with open("README.rst") as f:
    readme = f.read()

libcgaddag = CTypes("gaddag/libcgaddag",
                    sources=["gaddag/cGADDAG-0.4/src/cgaddag.c"],
                    extra_compile_args=["-O3"],
                    extra_link_args=["-lz"])

setup(name="GADDAG",
      version="0.4",
      description="Python wrapper of cGADDAG",
      long_description=readme,
      license="MIT",
      author="Jordan Bass",
      author_email="jordan+gaddag@jbass.io",
      url="https://github.com/jorbas/GADDAG",
      download_url="https://github.com/jorbas/GADDAG/archive/0.4.tar.gz",
      platforms="any",
      packages=["gaddag"],
      ext_modules=[libcgaddag],
      tests_require=["pytest"],
      cmdclass={"build_ext": build_ext},
      classifiers=[]
)
