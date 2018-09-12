# users

from cg_tornado import CgDbLogic
from app.cg_auth.models.data_models import UserCode


class Codes(CgDbLogic):

    def prepare(self):
        self.Model = UserCode
        super().prepare()
