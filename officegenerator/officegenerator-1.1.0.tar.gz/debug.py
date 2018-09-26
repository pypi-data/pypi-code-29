#!/usr/bin/python
import os
import officegenerator
os.system("python3 setup.py install --user")
from officegenerator.demo import main
main(['--create'])