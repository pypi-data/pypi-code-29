import setuptools
import platform, subprocess
import glob
import sys

is64bits = sys.maxsize > 2**32

if (is64bits and (platform.system()=='Linux' or platform.system()=='Darwin' or platform.system()=='Windows')):
        print("Installing...")
else:
	print("Unsupported Platform")
	exit(1)
subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, cwd="SoftFloat-master/build/Linux-x86_64-GCC/")
p=subprocess.Popen(["make"], stdout=subprocess.PIPE, cwd="SoftFloat-master/build/Linux-x86_64-GCC/")

with open("README.md", "r") as fh:
    long_description = fh.read()
p.communicate()

setuptools.setup(
    name="softfloat",
    version="0.1.3",
    author="Siew Hoon LEONG (Cerlane)",
    author_email="cerlane@posithub.org",
    description="SoftFloat Python Package",
    long_description="Berkeley SoftFloat Python Package",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cerlane/SoftFloat-Python",    
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    packages=setuptools.find_packages('SoftFloat-master/python'),
    package_dir={'':'SoftFloat-master/python'},
    py_modules =['softfloat'],
    ext_modules = [setuptools.Extension('_softfloat',
        sources = ['SoftFloat-master/python/softfloat_python_wrap.c'],# + glob.glob("SoftFloat-master/source/*.c"), 
        include_dirs = ["SoftFloat-master/source/include"],#, ".", "SoftFloat-master/source/8086-SSE", 'SoftFloat-master/build/Linux-x86_64-GCC'],
        #extra_compile_args = ["-DSOFTFLOAT_FAST_INT64", "-DSOFTFLOAT_ROUND_ODD", "-DINLINE_LEVEL=5", "-DSOFTFLOAT_FAST_DIV32TO16", "-DSOFTFLOAT_FAST_DIV64TO32"] )],
	extra_objects=['SoftFloat-master/build/Linux-x86_64-GCC/softfloat.a'])],
    data_files = [("", ["LICENSE"])]
)

