from setuptools import setup 
  
# reading long description from file 
with open('DESCRIPTION.txt') as file: 
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = [] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 4 - Beta', 
    'Intended Audience :: Developers', 
    'Topic :: Internet', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python', 
    'Programming Language :: Python :: 2', 
    'Programming Language :: Python :: 2.6', 
    'Programming Language :: Python :: 2.7', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    ] 
  
# calling the setup function  
setup(name='cipherText', 
      version='1.0.0', 
      description='encryption/decryption file for text files', 
      long_description=long_description, 
      url='https://github.com/Aniket8001/Cipher-v1.0', 
      author='Aniket Mahesh Alvekar', 
      author_email='aniketalvekar@gmail.com', 
      license='MIT', 
      packages=[], 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='Encryp Decryp'
      ) 
