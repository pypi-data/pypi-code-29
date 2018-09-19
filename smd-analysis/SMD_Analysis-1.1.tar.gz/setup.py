import setuptools
setuptools.setup(
    name="SMD_Analysis",
    version="1.1",
    author="rehab shahzadi",
    author_email="rehab.shahzadi@kics.edu.pk",
    description="An API for social media data analysis",
    packages=setuptools.find_packages(),

    classifiers = (
                  "Programming Language :: Python :: 3",
                  "Operating System :: OS Independent",
              ),
     install_requires=[
        'pandas==0.23.4',
        'nltk==3.3',
         'scikit-learn==0.19.2',
         'scipy==1.1.0',

    ],
)
