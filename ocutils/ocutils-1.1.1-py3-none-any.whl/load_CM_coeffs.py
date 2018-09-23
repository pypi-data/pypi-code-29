'''
Function to load Chen & Millero coefficients from a text file for SSP calculation.
Returns a dictionary of coefficients.
'''


def load_CM_coeffs(coeffs_file):

    coeffs = {}

    fi = open(coeffs_file, 'rt')
    els = fi.read().split()
    fi.close()

    nc = len(els)
    for n in range(0, nc, 2):
        coeffs[els[n]] = float(els[n + 1])

    return coeffs
