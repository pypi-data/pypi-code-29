import os
import numpy as np 
import time
def mask_remover(dirname):
	print('removing mask')
	if dirname[-1] != '/':
		dirname = dirname + '/'
	setnames =  [dirname + _ for _ in os.listdir(dirname) if 'set' in _]
	imagenames = []
	for setname in setnames:
		if setname[-1] != '/':
			setname = setname + '/' 
		imagename = [setname + _ for _ in os.listdir(setname) if 'image' in _]
		imagenames.append(imagename)
	imagenames = np.array(imagenames).flatten()
	for imagename in imagenames:
		if imagename[-1] != '/':
			imagename = imagename + '/' 
		images = [ _ for _ in os.listdir(imagename) if 'tiff' in _]
		images.remove('sum.tiff')
		images = [imagename + s for s in images]
		for image in images:
			os.remove(image)
