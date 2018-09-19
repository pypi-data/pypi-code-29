# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

""" script_run_config.py for handling script run configuration. """
from azureml._logging import ChainedIdentity
from ._experiment_method import experiment_method
from .runconfig import RunConfiguration


def submit(script_run_config, workspace, experiment_name):
    """
    :type script_run_config: ScriptRunConfig
    :type workspace: azureml.core.workspace.Workspace
    :type experiment_name: str
    """
    from azureml.core import Experiment
    from azureml._execution import _commands
    from azureml._project.project import Project

    experiment = Experiment(workspace, experiment_name)
    project = Project(directory=script_run_config.source_directory, experiment=experiment)

    # Gets a deep copy of run_config
    run_config = RunConfiguration._get_run_config_object(
        path=script_run_config.source_directory, run_config=script_run_config.run_config)

    if script_run_config.arguments:
        run_config.arguments = script_run_config.arguments

    # TODO: Add relative path magic
    if script_run_config.script:
        run_config.script = script_run_config.script

    return _commands.start_run(project, run_config,
                               telemetry_values=script_run_config._telemetry_values)


class ScriptRunConfig(ChainedIdentity):
    """
        A class for setting up configurations for script runs. Type: ChainedIdentity
    """
    @experiment_method(submit_function=submit)
    def __init__(self, source_directory, script=None, arguments=None, run_config=None, _telemetry_values=None):
        """
        :type source_directory: str
        :type script: str
        :type arguments: list
        :type run_config: RunConfiguration
        """
        self.source_directory = source_directory
        self.script = script
        self.arguments = arguments
        self.run_config = run_config if run_config else RunConfiguration()
        self._telemetry_values = _telemetry_values
