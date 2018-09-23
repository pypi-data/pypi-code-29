'''
Wrappers for the "MASShortcut" framework on macOS.

For documentation see https://github.com/shpakovski/MASShortcut
'''

from pyobjc_setup import setup, Extension
from setuptools import Command
from distutils import log
from distutils.command import build
from distutils.sysconfig import get_config_var
import os
import subprocess
import shlex
import shutil

VERSION="1.0a0"


class build_framework(Command):
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        log.info("Build MASShortcut framework")

        # XXX: The 'build' at the end should be dynamic...
        build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')


        # Detect the architectures this python was build for...
        cflags = shlex.split(get_config_var('CFLAGS'))
        archs = []
        try:
            start_idx = 0
            while True:
                idx = cflags.index('-arch', start_idx)
                archs.extend(["-arch", cflags[idx+1]])
                start_idx = idx + 2
        except ValueError:
            pass

        subprocess.check_call([
             "xcodebuild",
                "-scheme", "MASShortcut",
                "-configuration", "Release",
                "-derivedDataPath", build_dir,
                ] + archs + [
                "build" ], cwd='src/MASShortcut')

        if os.path.exists("Lib/MASShortcut/MASShortcut.framework"):
            shutil.rmtree("Lib/MASShortcut/MASShortcut.framework")
        os.rename(os.path.join(build_dir, "Build", "Products", "Release", "MASShortcut.framework"), "Lib/MASShortcut/MASShortcut.framework")

build.build.sub_commands.insert(0, ('build_framework', None))

setup(
    name='pyobjc-MASShortcut',
    description = "Wrappers for the library MASShortcut on macOS",
    packages = [ "MASShortcut" ],
    min_os_level = '10.9',
    ext_modules = [
        Extension('MASShortcut._inlines',
           [ 'Modules/_MASShortcut_inlines.m' ],
           extra_compile_args=["-FLib/MASShortcut"]
           )
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core',
        'pyobjc-framework-Cocoa',
    ],
    long_description=__doc__,
    cmdclass={
        'build_framework': build_framework
    },
)
