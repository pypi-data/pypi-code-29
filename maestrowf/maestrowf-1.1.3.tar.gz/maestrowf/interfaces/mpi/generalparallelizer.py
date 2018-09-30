from maestrowf.abstracts.interfaces import Parallelizer


class GeneralParallelizer(Parallelizer):
    """A class for general parallel command generation."""

    def __init__(self, cmd, recipe):
        """
        Construct an instance of the GeneralParallelizer.

        :param cmd: The parallel command to be used.
        :param recipe: A dictionary containing the generalized recipe format.
        """
        self._cmd = cmd
        self._recipe = recipe

    def get_parallelize_command(self, resources):
        """
        Generate the parallelization segement of the command line.

        :param resources: Dict of resources to be used by parallel commands.
        :returns: A string of the parallelize command configured using the
        specified resources.
        """
        _mpi_cmd = [self._cmd]
        for resource, value in resources.items():
            _mpi_cmd += [self._recipe["parameters"][resource], value]

        return " ".join(_mpi_cmd)
