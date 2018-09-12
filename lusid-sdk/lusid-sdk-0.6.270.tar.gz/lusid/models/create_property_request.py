# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CreatePropertyRequest(Model):
    """CreatePropertyRequest.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param scope:
    :type scope: str
    :param name:
    :type name: str
    :param value:
    :type value: object
    :param effective_from: Date for which the property is effective from
    :type effective_from: datetime
    :ivar unit:
    :vartype unit: str
    """

    _validation = {
        'value': {'required': True},
        'unit': {'readonly': True},
    }

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
        'effective_from': {'key': 'effectiveFrom', 'type': 'iso-8601'},
        'unit': {'key': 'unit', 'type': 'str'},
    }

    def __init__(self, value, scope=None, name=None, effective_from=None):
        super(CreatePropertyRequest, self).__init__()
        self.scope = scope
        self.name = name
        self.value = value
        self.effective_from = effective_from
        self.unit = None
