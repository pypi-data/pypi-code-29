# users
import json

from cg_tornado import CgDbLogic
from app.cg_auth.models.data_models import Group
from cg_tornado.errors import PermissionDenied


class Groups(CgDbLogic):

    def prepare(self):
        self.Model = Group
        super().prepare()

    def _process(self):
        if self.Data['group_id'] in ['1', 1]:
            raise PermissionDenied()

        if 'menu_permissions' in self.Data and self.Data['menu_permissions'] is not None:
            self.Data['menu_permissions'] = json.dumps(self.Data['menu_permissions'])

        # make compiled_permissions from updated menu_permissions
        # self.Data['compiled_permissions'] = '{}'

        return

    def ChildGroupIds(self, parent_id):
        records = self.gdb.query(Group).filter(Group.parent_id == parent_id).all()
        ids = [rec.group_id for rec in records]
        for rec in records:
            sub_ids = self.ChildGroupIds(rec.group_id)
            ids += sub_ids
        return ids

    def Create(self):
        self._process()
        return super().Create()

    def Update(self):
        self._process()
        return super().Update()

    def Single(self):
        data = super().Single()
        if data is not None:
            if 'menu_permissions' in data and data['menu_permissions'] is not None:
                data['menu_permissions'] = json.loads(data['menu_permissions'])

        return data

    def List(self):
        self.addTopWhere('group_id', 1, op='gt')
        return super().List()

    def Delete(self):
        self.AssertData('oid')
        oids = self.Data['oid']
        if not isinstance(oids, list):
            oids = [oids]

        if '1' in oids or 1 in oids:
            raise PermissionDenied()

        return super().Delete()

    def LoadSelectOptions(self):
        self.addTopWhere('group_id', 1, op='gt')
        return super().LoadSelectOptions()

    def FilterOptions(self):
        self.addTopWhere('group_id', 1, op='gt')
        return super().FilterOptions()
