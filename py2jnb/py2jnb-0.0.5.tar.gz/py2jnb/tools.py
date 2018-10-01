"""
Provide simplified entry points for common task
"""
from .converter import convert
from .reader import read
import logging

def python_to_notebook(input_filename, output_filename):
    """
    Convert the given python source file into a properly formatted notebook.
    """
    cvt = read(input_filename)
    convert(cvt, output_filename)
    logging.info("Convertered {} to {}".format(input_filename,output_filename))
