import setuptools
import platform, subprocess
import glob
import sys

#Check if SoftPosit is installed
zip_file_url='https://gitlab.com/cerlane/SoftPosit/-/archive/master/SoftPosit-master.zip'

is64bits = sys.maxsize > 2**32

if (is64bits and (platform.system()=='Linux' or platform.system()=='Darwin' or platform.system()=='Windows')):
        print("Installing...")
else:
	print("Unsupported Platform")
	exit(1)

#if sys.version_info >= (3, 0):
#    import requests, zipfile, io
#    r = requests.get(zip_file_url)
#    z = zipfile.ZipFile(io.BytesIO(r.content))
#    z.extractall()
#else:
#    import requests, zipfile, StringIO
#    r = requests.get(zip_file_url, stream=True)
#    z = zipfile.ZipFile(StringIO.StringIO(r.content))
#    z.extractall()

#softpositMod = setuptools.Extension('_softposit',
#        sources = ['SoftPosit-master/python/softposit_python_wrap.c'] + glob.glob("SoftPosit-master/source/*.c"),
#        include_dirs = ["SoftPosit-master/source/include", ".", 'SoftPosit-master/build/Linux-x86_64-GCC'])


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="softposit",
    version="0.3.3",
    author="Siew Hoon LEONG (Cerlane)",
    author_email="cerlane@posithub.org",
    description="SoftPosit Python Package",
    long_description="Next Generation Arithmetic SoftPosit Python Package",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cerlane/SoftPosit-Python",    
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    packages=setuptools.find_packages('SoftPosit-master/python'),
    package_dir={'':'SoftPosit-master/python'},
    py_modules =['softposit'],
    ext_modules = [setuptools.Extension('_softposit',
        sources = ['SoftPosit-master/python/softposit_python_wrap.c'] + glob.glob("SoftPosit-master/source/*.c"),
        extra_compile_args = ["-std=gnu99"],
        include_dirs = ["SoftPosit-master/source/include", ".", 'SoftPosit-master/build/Linux-x86_64-GCC'])],
    data_files = [("", ["LICENSE"])]
)

