# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BatchBatchResponseDTO(Model):
    """BatchBatchResponseDTO.

    :param batch_id:
    :type batch_id: int
    :param batch_code:
    :type batch_code: str
    :param is_open:
    :type is_open: bool
    :param start_date:
    :type start_date: datetime
    :param end_date:
    :type end_date: datetime
    :param bill_count:
    :type bill_count: int
    :param running_total:
    :type running_total: float
    :param statement_date:
    :type statement_date: str
    :param due_date:
    :type due_date: str
    :param next_reading:
    :type next_reading: str
    :param control_code:
    :type control_code: str
    :param invoice_number:
    :type invoice_number: str
    :param account_period_name:
    :type account_period_name: str
    :param account_period_number:
    :type account_period_number: int
    :param account_period_year:
    :type account_period_year: int
    :param note:
    :type note: str
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserUserChildDTO
    """

    _attribute_map = {
        'batch_id': {'key': 'batchId', 'type': 'int'},
        'batch_code': {'key': 'batchCode', 'type': 'str'},
        'is_open': {'key': 'isOpen', 'type': 'bool'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'bill_count': {'key': 'billCount', 'type': 'int'},
        'running_total': {'key': 'runningTotal', 'type': 'float'},
        'statement_date': {'key': 'statementDate', 'type': 'str'},
        'due_date': {'key': 'dueDate', 'type': 'str'},
        'next_reading': {'key': 'nextReading', 'type': 'str'},
        'control_code': {'key': 'controlCode', 'type': 'str'},
        'invoice_number': {'key': 'invoiceNumber', 'type': 'str'},
        'account_period_name': {'key': 'accountPeriodName', 'type': 'str'},
        'account_period_number': {'key': 'accountPeriodNumber', 'type': 'int'},
        'account_period_year': {'key': 'accountPeriodYear', 'type': 'int'},
        'note': {'key': 'note', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'UserUserChildDTO'},
    }

    def __init__(self, batch_id=None, batch_code=None, is_open=None, start_date=None, end_date=None, bill_count=None, running_total=None, statement_date=None, due_date=None, next_reading=None, control_code=None, invoice_number=None, account_period_name=None, account_period_number=None, account_period_year=None, note=None, created_by=None):
        super(BatchBatchResponseDTO, self).__init__()
        self.batch_id = batch_id
        self.batch_code = batch_code
        self.is_open = is_open
        self.start_date = start_date
        self.end_date = end_date
        self.bill_count = bill_count
        self.running_total = running_total
        self.statement_date = statement_date
        self.due_date = due_date
        self.next_reading = next_reading
        self.control_code = control_code
        self.invoice_number = invoice_number
        self.account_period_name = account_period_name
        self.account_period_number = account_period_number
        self.account_period_year = account_period_year
        self.note = note
        self.created_by = created_by
