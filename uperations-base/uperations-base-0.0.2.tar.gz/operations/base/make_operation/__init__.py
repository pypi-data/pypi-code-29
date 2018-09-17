

from uperations.operation import Operation
from ..utils import operation_create

class MakeOperation(Operation):

    @staticmethod
    def name():
        return "make_operation"

    @staticmethod
    def description():
        return "Create a new operation"

    def _parser(self, main_parser):
        main_parser.add_argument('library', help="Name of the library to add the operation")
        main_parser.add_argument('operation', help="Name of the operation")
        return

    def _run(self):
        operation_create('operations',self.args.library,self.args.operation)
        return