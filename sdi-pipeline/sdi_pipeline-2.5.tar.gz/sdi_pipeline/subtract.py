from initialize import loc
from master_residual import MR
import subtract_hotpants
import subtract_ibi
import subtract_numpy

if __name__ == '__main__':
    path = input("\nEnter path to exposure time directory: ")
    method = input("\nChoose subtraction method: numpy (default), hotpants, image-by-image, or iraf: ")
    if method == 'numpy' or method == '':
        subtract_numpy.subtract2(path)
        MR(path)
    elif method == 'hotpants':
        subtract_hotpants.hotpants(path)
        MR(path)
    elif method == 'image-by-image':
        subtract_ibi.subtract3(path)
        MR(path)
    elif method == 'iraf':
        import subtract_iraf
        subtract_iraf.subtract(path)
        MR(path)
    else:
        print("\nError: Unknown method")