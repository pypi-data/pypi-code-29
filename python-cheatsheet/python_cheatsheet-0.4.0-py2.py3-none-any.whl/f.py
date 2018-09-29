# -*- coding: utf-8 -*-

"""Main module."""

# File
def files():
    filename = "hello.txt"
    file = open(filename, "w")
    for line in file:
        print( line );
    file.close();


#facial recognition
#pip install cmake
#pip install opencv-python
#pip install face_recognition
# add image
# run file !  BOOM facial recogition
