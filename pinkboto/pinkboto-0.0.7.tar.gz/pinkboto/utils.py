def to_csv(dics, filename, keys=None):
    """
    Create a CSV from a dictionary list
    :param dics: dictionary list
    :param filename: output filename
    :param keys: Optional, subset of keys. Default is all keys.
    :return: None
    """
    if isinstance(dics, dict):
        dics = [dics]

    if not keys:
        keys = sorted(set().union(*(d.keys() for d in dics)))

    import csv
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dics)
