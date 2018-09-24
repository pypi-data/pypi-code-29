from distutils.core import setup, Extension

#import distutils.log
#distutils.log.set_verbosity(distutils.log.DEBUG) # Set DEBUG level

pyepd = Extension('EPD',
                    sources = ['src/lz.c','src/EPD.c','src/Compression.c','src/Type0.c','src/Type2.c'],
                    include_dirs=['include/',]
                  )

setup (name = 'EPD',
       version = '1.2',
       author="Paweł Musiał, MpicoSys (www.mpicosys.com)",
       author_email='pawel.musial@mpicosys.com',
       description = 'EPD library for MpicoSys Timing Controllers (TC/TCM)',
       ext_modules = [pyepd,])