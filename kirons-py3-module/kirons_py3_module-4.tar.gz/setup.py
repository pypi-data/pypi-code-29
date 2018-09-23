import setuptools

old  = open("version.txt").read()
new = open("version.txt","w+")
new.write(str(int(int(old)+1)))
new.close()

setuptools.setup(
    name="kirons_py3_module",
    version=open("version.txt").read(),
    author="KironDevCoder",
    author_email="mojanghouse@gmail.com",
    description="A simple module made by KironDevCoder for hard-to-program programs",
    long_description="A simple module made by KironDevCoder for hard-to-program programs",
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
