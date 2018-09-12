# employees_logic

from cg_tornado import CgDbLogic
from cg_tornado.models.data_models import FileAttachment


class Attachments(CgDbLogic):

    def prepare(self):
        self.Model = FileAttachment
        self.PublicMethods = ['Attach', 'List', 'Delete']

        super().prepare()
