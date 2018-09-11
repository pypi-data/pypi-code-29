# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewChargebackWorkflowChargebackWorkflowResponseDTO(Model):
    """ChargebackNewChargebackWorkflowChargebackWorkflowResponseDTO.

    :param chargeback_workflow_steps: List of workflow steps with details
    :type chargeback_workflow_steps:
     list[~energycap.sdk.models.ChargebackNewChargebackWorkflowChargebackWorkflowStepDTO]
    :param chargeback_workflow_id: Identifier for the chargeback workflow
    :type chargeback_workflow_id: int
    :param chargeback_workflow_info: Name given to the chargeback workflow
    :type chargeback_workflow_info: str
    """

    _attribute_map = {
        'chargeback_workflow_steps': {'key': 'chargebackWorkflowSteps', 'type': '[ChargebackNewChargebackWorkflowChargebackWorkflowStepDTO]'},
        'chargeback_workflow_id': {'key': 'chargebackWorkflowId', 'type': 'int'},
        'chargeback_workflow_info': {'key': 'chargebackWorkflowInfo', 'type': 'str'},
    }

    def __init__(self, chargeback_workflow_steps=None, chargeback_workflow_id=None, chargeback_workflow_info=None):
        super(ChargebackNewChargebackWorkflowChargebackWorkflowResponseDTO, self).__init__()
        self.chargeback_workflow_steps = chargeback_workflow_steps
        self.chargeback_workflow_id = chargeback_workflow_id
        self.chargeback_workflow_info = chargeback_workflow_info
