

from uperations.library import Library
from .make_library import Makelibrary
from .make_operation import MakeOperation
from .make_operationtype import MakeOperationType
from .list_operation import Listoperation
from .yaml_to_json import Yamltojson
from .publish import Publish
from .command import Command
from .dockerfile import Dockerfile
from .helloworld import Helloworld
from .hello_name import HelloName

class Base(Library):

    @staticmethod
    def name():
        return "base"

    @staticmethod
    def description():
        return "General operations"

    def operations(self):
        return {
            'hello:world': Helloworld(self),
            'make:library': Makelibrary(self),
            'make:operation': MakeOperation(self),
            'make:operation:type': MakeOperationType(self),
            'list:operations': Listoperation(self),
            'yaml_to_json': Yamltojson(self),
            'publish': Publish(self),
            'command': Command(self),
            'dockerfile': Dockerfile(self),
            'hello': HelloName(self)
        }