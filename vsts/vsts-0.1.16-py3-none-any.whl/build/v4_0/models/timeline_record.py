# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class TimelineRecord(Model):
    """TimelineRecord.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param change_id:
    :type change_id: int
    :param current_operation:
    :type current_operation: str
    :param details:
    :type details: :class:`TimelineReference <build.v4_0.models.TimelineReference>`
    :param error_count:
    :type error_count: int
    :param finish_time:
    :type finish_time: datetime
    :param id:
    :type id: str
    :param issues:
    :type issues: list of :class:`Issue <build.v4_0.models.Issue>`
    :param last_modified:
    :type last_modified: datetime
    :param log:
    :type log: :class:`BuildLogReference <build.v4_0.models.BuildLogReference>`
    :param name:
    :type name: str
    :param order:
    :type order: int
    :param parent_id:
    :type parent_id: str
    :param percent_complete:
    :type percent_complete: int
    :param result:
    :type result: object
    :param result_code:
    :type result_code: str
    :param start_time:
    :type start_time: datetime
    :param state:
    :type state: object
    :param task:
    :type task: :class:`TaskReference <build.v4_0.models.TaskReference>`
    :param type:
    :type type: str
    :param url:
    :type url: str
    :param warning_count:
    :type warning_count: int
    :param worker_name:
    :type worker_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'change_id': {'key': 'changeId', 'type': 'int'},
        'current_operation': {'key': 'currentOperation', 'type': 'str'},
        'details': {'key': 'details', 'type': 'TimelineReference'},
        'error_count': {'key': 'errorCount', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'log': {'key': 'log', 'type': 'BuildLogReference'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'result': {'key': 'result', 'type': 'object'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'object'},
        'task': {'key': 'task', 'type': 'TaskReference'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'warning_count': {'key': 'warningCount', 'type': 'int'},
        'worker_name': {'key': 'workerName', 'type': 'str'}
    }

    def __init__(self, _links=None, change_id=None, current_operation=None, details=None, error_count=None, finish_time=None, id=None, issues=None, last_modified=None, log=None, name=None, order=None, parent_id=None, percent_complete=None, result=None, result_code=None, start_time=None, state=None, task=None, type=None, url=None, warning_count=None, worker_name=None):
        super(TimelineRecord, self).__init__()
        self._links = _links
        self.change_id = change_id
        self.current_operation = current_operation
        self.details = details
        self.error_count = error_count
        self.finish_time = finish_time
        self.id = id
        self.issues = issues
        self.last_modified = last_modified
        self.log = log
        self.name = name
        self.order = order
        self.parent_id = parent_id
        self.percent_complete = percent_complete
        self.result = result
        self.result_code = result_code
        self.start_time = start_time
        self.state = state
        self.task = task
        self.type = type
        self.url = url
        self.warning_count = warning_count
        self.worker_name = worker_name
