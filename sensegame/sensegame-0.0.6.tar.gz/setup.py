import setuptools

setuptools.setup(
    name="sensegame",
    version="0.0.6",
    author="Jorn Bersvendsen",
    description="Helper library for developing games with the SenseHAT on the Raspberry PI",
    license="MIT",
    keywords=[
        "sense hat",
        "raspberrypi",
        "game"
    ],
    url="https://github.com/jornb/sensegame",
    install_requires=[
        "evdev"
    ],
    python_requires=">=3",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment",
        "Topic :: Education",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    packages=["sensegame"]
)
