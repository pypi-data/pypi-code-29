from setuptools import setup

setup(name='ie_mbdbl2018_ahirane',
      version='0.2',  # Development release
      description='Python package to use the method of linear congruences to generate a random number',
      long_description="""The package provides a function called linear_congruence_random_generator(), wich returns a randon number based on the method of linear congruences using the following parameters:
a = 22695477
b = 1
m = 2**32
x0=1649836483

Also it provides and object called c_linear_congruences. 
It should be intialized providing the parameters x0,a,b and m. 
The object provides a method called linear_congruence_random_generator() 
wich will return a random number based on the method of linear congruences 
using the parameters of the object initialization.
""",
      url='https://github.com/ahirane/Method_of_linear_congruences',
      author='Andres Hirane',
      author_email='ahirane@student.ie.edu',
      license='MIT',
          packages=['ie_mbdbl2018_ahirane'],
      zip_safe=False)