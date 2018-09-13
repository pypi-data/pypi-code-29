# Filename: attachments

from cg_tornado import CGDbLogic
from cg_tornado.models.data_models import FileAttachment


class Attachments(CGDbLogic):

    def prepare(self):
        self.Model = FileAttachment
        self.PublicMethods = ['Attach', 'List', 'Delete']

        super().prepare()
