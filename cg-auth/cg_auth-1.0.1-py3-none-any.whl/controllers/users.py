# users
from sqlalchemy import func

from cg_tornado import CgDbLogic
from app.cg_auth.models.data_models import User
from cg_tornado.errors import PermissionDenied


class Users(CgDbLogic):

    def prepare(self):
        self.Model = User
        self.PublicMethods = []

        super().prepare()

    def Create(self):
        if 'password' in self.Data:
            self.Data['password'] = func.md5(self.Data['password'])
        self.Data['is_activated'] = True
        return super().Create()

    def Update(self):
        if 'password' in self.Data:
            if self.Data['password'] != '<<<encrypted>>>':
                self.Data['password'] = func.md5(self.Data['password'])
            else:
                self.Data.pop('password')

        return super().Update()

    def Single(self):
        data = super().Single()
        return data

    def Delete(self):
        self.AssertData('oid')
        oids = self.Data['oid']
        if not isinstance(oids, list):
            oids = [oids]

        if '1' in oids or 1 in oids:
            raise PermissionDenied()

        return super().Delete()
