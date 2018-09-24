from setuptools import setup

setup(name='chaton',
      version='0.1.2',
      description='A small chatbot for social robots',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
      ],
      keywords='chatbot robot',
      url='https://gitlab.com/etri_hmi/chaton',
      author='Minsu Jang',
      author_email='minsu@etri.re.kr',
      license='GPL 3.0',
      packages=['chaton'],
      install_requires=[
          'lark-parser',
      ],
      zip_safe=False)