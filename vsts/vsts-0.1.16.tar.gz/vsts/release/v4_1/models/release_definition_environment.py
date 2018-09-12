# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ReleaseDefinitionEnvironment(Model):
    """ReleaseDefinitionEnvironment.

    :param badge_url:
    :type badge_url: str
    :param conditions:
    :type conditions: list of :class:`Condition <release.v4_1.models.Condition>`
    :param demands:
    :type demands: list of :class:`object <release.v4_1.models.object>`
    :param deploy_phases:
    :type deploy_phases: list of :class:`object <release.v4_1.models.object>`
    :param deploy_step:
    :type deploy_step: :class:`ReleaseDefinitionDeployStep <release.v4_1.models.ReleaseDefinitionDeployStep>`
    :param environment_options:
    :type environment_options: :class:`EnvironmentOptions <release.v4_1.models.EnvironmentOptions>`
    :param execution_policy:
    :type execution_policy: :class:`EnvironmentExecutionPolicy <release.v4_1.models.EnvironmentExecutionPolicy>`
    :param id:
    :type id: int
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <release.v4_1.models.IdentityRef>`
    :param post_deploy_approvals:
    :type post_deploy_approvals: :class:`ReleaseDefinitionApprovals <release.v4_1.models.ReleaseDefinitionApprovals>`
    :param post_deployment_gates:
    :type post_deployment_gates: :class:`ReleaseDefinitionGatesStep <release.v4_1.models.ReleaseDefinitionGatesStep>`
    :param pre_deploy_approvals:
    :type pre_deploy_approvals: :class:`ReleaseDefinitionApprovals <release.v4_1.models.ReleaseDefinitionApprovals>`
    :param pre_deployment_gates:
    :type pre_deployment_gates: :class:`ReleaseDefinitionGatesStep <release.v4_1.models.ReleaseDefinitionGatesStep>`
    :param process_parameters:
    :type process_parameters: :class:`ProcessParameters <release.v4_1.models.ProcessParameters>`
    :param properties:
    :type properties: :class:`object <release.v4_1.models.object>`
    :param queue_id:
    :type queue_id: int
    :param rank:
    :type rank: int
    :param retention_policy:
    :type retention_policy: :class:`EnvironmentRetentionPolicy <release.v4_1.models.EnvironmentRetentionPolicy>`
    :param run_options:
    :type run_options: dict
    :param schedules:
    :type schedules: list of :class:`ReleaseSchedule <release.v4_1.models.ReleaseSchedule>`
    :param variable_groups:
    :type variable_groups: list of int
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'badge_url': {'key': 'badgeUrl', 'type': 'str'},
        'conditions': {'key': 'conditions', 'type': '[Condition]'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deploy_phases': {'key': 'deployPhases', 'type': '[object]'},
        'deploy_step': {'key': 'deployStep', 'type': 'ReleaseDefinitionDeployStep'},
        'environment_options': {'key': 'environmentOptions', 'type': 'EnvironmentOptions'},
        'execution_policy': {'key': 'executionPolicy', 'type': 'EnvironmentExecutionPolicy'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'post_deployment_gates': {'key': 'postDeploymentGates', 'type': 'ReleaseDefinitionGatesStep'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'pre_deployment_gates': {'key': 'preDeploymentGates', 'type': 'ReleaseDefinitionGatesStep'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'properties': {'key': 'properties', 'type': 'object'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'EnvironmentRetentionPolicy'},
        'run_options': {'key': 'runOptions', 'type': '{str}'},
        'schedules': {'key': 'schedules', 'type': '[ReleaseSchedule]'},
        'variable_groups': {'key': 'variableGroups', 'type': '[int]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, badge_url=None, conditions=None, demands=None, deploy_phases=None, deploy_step=None, environment_options=None, execution_policy=None, id=None, name=None, owner=None, post_deploy_approvals=None, post_deployment_gates=None, pre_deploy_approvals=None, pre_deployment_gates=None, process_parameters=None, properties=None, queue_id=None, rank=None, retention_policy=None, run_options=None, schedules=None, variable_groups=None, variables=None):
        super(ReleaseDefinitionEnvironment, self).__init__()
        self.badge_url = badge_url
        self.conditions = conditions
        self.demands = demands
        self.deploy_phases = deploy_phases
        self.deploy_step = deploy_step
        self.environment_options = environment_options
        self.execution_policy = execution_policy
        self.id = id
        self.name = name
        self.owner = owner
        self.post_deploy_approvals = post_deploy_approvals
        self.post_deployment_gates = post_deployment_gates
        self.pre_deploy_approvals = pre_deploy_approvals
        self.pre_deployment_gates = pre_deployment_gates
        self.process_parameters = process_parameters
        self.properties = properties
        self.queue_id = queue_id
        self.rank = rank
        self.retention_policy = retention_policy
        self.run_options = run_options
        self.schedules = schedules
        self.variable_groups = variable_groups
        self.variables = variables
