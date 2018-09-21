import h5py as h5
from PIL import Image
from six import BytesIO

with h5.File('recon.emd', 'r') as f:
    emdgrp = f['data/tomography']
    data = emdgrp['data'][:]
    slices = []
    for slice in data:
        print('slice')
        slices.append(Image.fromarray(slice, mode='F'))

    io = BytesIO()
    slices[0].save('test.tif', format='tiff', compression='tiff_deflate',  save_all=True, append_images=slices[1:])
