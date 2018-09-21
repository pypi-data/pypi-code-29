import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setuptools.setup(
    name="pydecisions",
    version="0.1.3",
    author="Balamurali M",
    author_email="balamurali9m@gmail.com",
	url='http://balamurali-m.com/',
    description="pydecisions - Python Library with a some management decision making techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
		"Intended Audience :: Education",
        "Intended Audience :: Information Technology",
		"Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
		"Topic :: Education",
		"Topic :: Scientific/Engineering :: Mathematics",
		"Topic :: Scientific/Engineering :: Artificial Intelligence",
		"Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",		
        "Operating System :: OS Independent",
    ],  
)

