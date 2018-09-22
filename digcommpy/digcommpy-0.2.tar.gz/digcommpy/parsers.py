import ast

def _pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def read_simulation_log(filename):
    """Read a results file from a CustomSimulation.

    Parameters
    ----------
    filename : str
        File path or file object

    Returns
    -------
    results : dict
        Dict of all the results as returned from the original simulation.
    """
    with open(filename) as input_file:
        lines = input_file.readlines()
    sim_attr = lines.pop(0)
    enc_opt = ast.literal_eval(lines.pop(0))
    dec_opt = ast.literal_eval(lines.pop(0))
    mod_opt = ast.literal_eval(lines.pop(0))
    demod_opt = ast.literal_eval(lines.pop(0))
    test_opt = ast.literal_eval(lines.pop(0))
    results = {}
    for _key, _value in _pairwise(lines):
        key = ast.literal_eval(_key)
        value = ast.literal_eval(_value)
        results[key] = value
    return results
