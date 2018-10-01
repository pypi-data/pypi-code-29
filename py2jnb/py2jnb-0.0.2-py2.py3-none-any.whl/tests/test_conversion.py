import os
from py2nb.tools import python_to_notebook

def test_convert():
    print("\nSTART TEST")
    SAMPLE_DIR = os.path.join(os.getcwd(),'samples')

    INPUT_FNAME = 'hello.py'
    BASENAME, _ = os.path.splitext(INPUT_FNAME)
    INPUT_PY = os.path.join(SAMPLE_DIR,INPUT_FNAME)
    print("Input file:",INPUT_PY)
    assert os.path.exists(INPUT_PY)

    OUTPUT_IPYNB = os.path.join(SAMPLE_DIR,BASENAME+".ipynb")
    print("Output file: ", OUTPUT_IPYNB)
    if os.path.exists(OUTPUT_IPYNB):
        os.remove(OUTPUT_IPYNB)

    python_to_notebook(INPUT_PY,OUTPUT_IPYNB)
    assert os.path.exists(OUTPUT_IPYNB)

    # os.remove(OUTPUT_IPYNB)


def test_cells_convert():
    SAMPLE_DIR = os.path.join(os.getcwd(), 'samples')

    INPUT_FNAME = 'hello_cells.py'
    BASENAME, _ = os.path.splitext(INPUT_FNAME)
    INPUT_PY = os.path.join(SAMPLE_DIR, INPUT_FNAME)
    print("Input file:", INPUT_PY)
    assert os.path.exists(INPUT_PY)

    OUTPUT_IPYNB = os.path.join(SAMPLE_DIR, BASENAME + ".ipynb")
    print("Output file: ", OUTPUT_IPYNB)
    if os.path.exists(OUTPUT_IPYNB):
        os.remove(OUTPUT_IPYNB)

    python_to_notebook(INPUT_PY,OUTPUT_IPYNB)
    assert os.path.exists(OUTPUT_IPYNB)

    # os.remove(OUTPUT_IPYNB)