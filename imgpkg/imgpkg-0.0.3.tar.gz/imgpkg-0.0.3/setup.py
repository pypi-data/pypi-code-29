import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imgpkg",
    version="0.0.3",
    author="TWQ",
    author_email="icedb001@gmail.com",
    description="A small images package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://en.gravatar.com/icee916",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'flickrapi',
        'google_images_download',
        'instaloader',
        'google_streetview',
        'zhconv',
        'torchvision',
        'opencv-python',
		'selenium',
		'pandas'
		'beautifulsoup4',
    ]
)