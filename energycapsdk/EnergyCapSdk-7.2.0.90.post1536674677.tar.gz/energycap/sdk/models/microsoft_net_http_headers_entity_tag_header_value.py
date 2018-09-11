# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftNetHttpHeadersEntityTagHeaderValue(Model):
    """MicrosoftNetHttpHeadersEntityTagHeaderValue.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar tag:
    :vartype tag:
     ~energycap.sdk.models.MicrosoftExtensionsPrimitivesStringSegment
    :ivar is_weak:
    :vartype is_weak: bool
    """

    _validation = {
        'tag': {'readonly': True},
        'is_weak': {'readonly': True},
    }

    _attribute_map = {
        'tag': {'key': 'tag', 'type': 'MicrosoftExtensionsPrimitivesStringSegment'},
        'is_weak': {'key': 'isWeak', 'type': 'bool'},
    }

    def __init__(self):
        super(MicrosoftNetHttpHeadersEntityTagHeaderValue, self).__init__()
        self.tag = None
        self.is_weak = None
