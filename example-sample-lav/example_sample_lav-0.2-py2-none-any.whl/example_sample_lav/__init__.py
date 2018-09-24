import numpy as np
from .text import joke
class array():
	a = np.array([1, 2, 3])   # Create a rank 1 array
	print(type(a))            # Prints "<class 'numpy.ndarray'>"
	print(a.shape)            # Prints "(3,)"
	print(a[0], a[1], a[2])   # Prints "1 2 3"
	a[0] = 5                  # Change an element of the array
	print(a)                  # Prints "[5, 2, 3]"

print joke