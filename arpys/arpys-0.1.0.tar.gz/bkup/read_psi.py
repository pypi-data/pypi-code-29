#!/usr/bin/python2
""" 
jScript to demonstrate the principles necessary to open and plot data
from an hdf5 file at the example of data from the SIS experiment at the SLS at
the PSI. 
"""
import h5py
import matplotlib.pyplot as plt

# Define path to file and filename
datapath = '/home/kevin/Documents/lqmr/materials/LSCO22/'
filename = 'LSCO22_2_0020.h5'

# Read the hdf5 formatted file
datfile = h5py.File(datapath+filename, 'r')

def print_field(field) :
    """ Helper function as argument for h5pyFile.visit(). """
    # Split the field into its parts, spearated by slashes
    parts = field.split('/')
    
    # The number of slashes is the number of parts minus 1
    nslashes = len(parts) - 1

    # Indent output proportional to the fields depth in the file structure
    indent = '    '
    print(nslashes * indent + parts[-1])

# Traverse all fields
datfile.visit(print_field)

# Extract the actual data
data = datfile['Electron Analyzer/Image Data']

# Extract the first cut
d0 = data[:,:,0]

# Plot it as a pseudocolormesh
fig = plt.figure()
mesh = plt.pcolormesh(d0)

plt.show()
