# Filename: user_codes

from cg_tornado import CGDbLogic
from cg_auth.models.data_models import UserCode


class UserCodes(CGDbLogic):

    def prepare(self):
        self.Model = UserCode
        super().prepare()
