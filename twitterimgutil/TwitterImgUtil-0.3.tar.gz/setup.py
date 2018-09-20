from setuptools import setup, find_packages

setup(name='TwitterImgUtil',
      version='0.3',
      description='include twitter images grabbing, adding labels function',
      url='https://github.com/BrefCool/TwitterImgUtil',
      author='bref',
      author_email='syx525@bu.edu',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
      ],
      packages=find_packages(),
      install_requires=['tweepy', 'Pillow', 'google-cloud-videointelligence', 'google-cloud-vision'],
      zip_safe=False)