import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vbx_vk",
    version="0.1",
    author="Valentine Bobrovsky",
    author_email="vbabrouski@outlook.com",
    license="MIT",
    description="vk_api for retards",
    url="https://github.com/vbxx3/vbx_vk",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['vk_api'],
)
