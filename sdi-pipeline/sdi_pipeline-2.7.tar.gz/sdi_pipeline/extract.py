import sex
import psf

def EXTRACT():
    path = input("-> Enter path to target's exposure time directory: ")
    sex.sextractor_psf(path)
    psf.psfex(path)
    sex.sextractor(path)
    sex.src_filter(path)

if __name__ == '__main__':
    path = input("-> Enter path to target's exposure time directory: ")
    sex.sextractor_psf(path)
    psf.psfex(path)
    sex.sextractor(path)
    sex.src_filter(path)