import cobra
import os
from gsmodutils.utils.scrumpy import load_scrumpy_model
from gsmodutils.exceptions import MediumError


def load_model(path, file_format=None):
    """
    Model loading that accepts multiple formats. Implemented to move away from dependency on cameo.load_model which,
    while good for users, created problems in testing.
    :str path: path to model
    :str or None file_format: format model is imported in if None, attemps to guess
    :return: cobra_model
    """
    if not os.path.exists(path):
        raise IOError('File {} not found'.format(path))

    if file_format is None:
        # Guess the file_format from extension
        file_format = os.path.splitext(path)[1][1:].strip().lower()

    if file_format == "json":
        cobra_model = cobra.io.load_json_model(path)
    elif file_format == "yaml":
        cobra_model = cobra.io.load_yaml_model(path)
    elif file_format in ["sbml", "xml"]:
        cobra_model = cobra.io.read_sbml_model(path)
    elif file_format in ["mat", "m", "matlab"]:
        cobra_model = cobra.io.load_matlab_model(path)
    elif file_format in ['spy', 'scrumpy']:
        cobra_model = load_scrumpy_model(path)
    else:
        raise TypeError('Cannot load file format {}'.format(file_format))

    return cobra_model


def load_medium(model, medium_dict, copy=False):
    """
    Load the medium of a model
    :param model: cobra.Model instance
    :param medium_dict: dictionary
    :param copy: Boolean: return copy of model
    :return:
    """

    if not isinstance(medium_dict, dict):
        raise TypeError("Expected python dictionary, got {} instead".format(type(medium_dict)))

    if not isinstance(model, cobra.Model):
        raise TypeError("Expected cobra model, got {} instead".format(type(model)))

    if copy:
        model = model.copy()

    bounds_store = dict()

    def _reset():
        """ Reset changes to model """
        if copy:
            # No point doing this if the model is a copy as the main function should throw an exception
            return

        for ex, bounds in bounds_store.items():
            ex_r = model.reactions.get_by_id(ex)
            ex_r.bounds = bounds

    for r, rate in medium_dict.items():
        try:
            ex_reaction = model.reactions.get_by_id(r)
            # Reaction should be an exchange reaction
            if ex_reaction not in model.exchanges:
                _reset()
                raise MediumError("Reaction {} is not an exchange".format(r))

            # Set reaction bounds
            bounds_store[ex_reaction.id] = ex_reaction.bounds
            ex_reaction.bounds = (rate, rate)
        except KeyError:
            _reset()
            raise MediumError("Reaction {} not found in model".format(r))

    return model
