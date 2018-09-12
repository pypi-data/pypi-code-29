# users

from cg_tornado import CgDbLogic
from app.cg_auth.models.data_models import UserDevice


class Devices(CgDbLogic):

    def prepare(self):
        self.Model = UserDevice
        super().prepare()

        self.PublicMethods = ['List', 'Delete']

    def List(self):
        self.addTopWhere(column='user_id', value=self.User.user_id)
        return super().List()
