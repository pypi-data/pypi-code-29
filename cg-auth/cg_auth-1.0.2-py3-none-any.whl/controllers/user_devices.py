# Filename: user_devices

from cg_tornado import CGDbLogic
from cg_auth.models.data_models import UserDevice


class UserDevices(CGDbLogic):

    def prepare(self):
        self.Model = UserDevice
        super().prepare()

        self.PublicMethods = ['List', 'Delete']

    def List(self):
        self.addTopWhere(column='user_id', value=self.User.user_id)
        return super().List()
