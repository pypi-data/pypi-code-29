# -*- coding: utf-8 -*-

"""Main module."""

# File
filename = "hello.txt"
file = open(filename, "w")
for line in file:
   print( line );
file.close();