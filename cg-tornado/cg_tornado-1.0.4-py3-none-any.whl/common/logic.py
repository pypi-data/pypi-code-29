# Filename: logic.py

import uuid
import random
import string

from sqlalchemy.exc import IntegrityError

from .helper import CGDbHelper
from cg_tornado.errors import RequiredFieldMissing, ChildRecordExists, ExceptionWithMessage


class CGDbLogic:
    def __init__(self, gdb, data=None, request=None, user=None, app=None):
        self.application = app
        self.User = user
        self.request = request
        self.gdb = gdb

        self.Data = data if data is not None else {}

        self.Model = None
        self.dbh = None
        self.PublicMethods = []

    def prepare(self):

        if self.Model is not None and self.gdb is not None:
            self.dbh = CGDbHelper(self.gdb, self.Model)
        else:
            pass  # raise exception

        self.PublicMethods.extend(['List', 'Single', 'Create', 'Update', 'Delete',
                                   'FilterOptions', 'SelectOptions', 'Attach'])

    def _loadController(self, slug, data=None):
        if slug not in self.application.Registry:
            raise ExceptionWithMessage('How dare you ???')

        Controller = self.application.Registry[slug]['ctrl']
        ctrl = Controller(gdb=self.gdb, data=data, request=self.request, user=self.User,
                                    app=self.application)
        ctrl.prepare()

        return ctrl

    def isSuperAdmin(self):
        return self.User.user_id == 1

    # Utility Methods
    def AssertData(self, *keys):
        for key in keys:
            if key not in self.Data or self.Data[key] is None:
                raise KeyError(key)
        return

    def AssertDataWithCleaning(self, *keys):
        for key in keys:
            if key not in self.Data or self.Data[key] is None:
                raise KeyError(key)

        for key in self.Data:
            if not any(key in k for k in keys):
                self.Data[key] = None
        return

    def GetUniqueId(self):
        return str(uuid.uuid4()).replace("-", "")

    def GetUniqueCode(self):
        return ''.join(random.choice(string.digits) for _ in range(4))

    def addTopOrder(self, column, direction):

        top_orders = [{
            'column': column,
            'dir': direction
        }]

        orders = self.Data['order'] if 'order' in self.Data else {}
        if len(orders) > 0:
            orders = top_orders + orders
        else:
            orders = top_orders

        self.Data['order'] = orders
        return

    def addTopWhere(self, column, value, op='eq'):
        wheres = self.Data['where'] if 'where' in self.Data else {}
        if len(wheres) == 0:
            wheres = {
                'column': column,
                'search': value,
                'op': op
            }
        else:
            wh2 = {
                'group': 'and',
                'children': [{
                    "column": column,
                    "search": value,
                    "op": op
                }],
            }

            wh2['children'].append(wheres)
            wheres = wh2

        self.Data['where'] = wheres
        return

    def _attachFile(self, data):
        from cg_tornado.models import UserFile, FileAttachment

        query = self.gdb.query(UserFile).filter(UserFile.file_id == data['file_id'])
        file = query.one_or_none()
        file.is_attached = True

        attachment = FileAttachment()
        attachment.file_id = data['file_id']
        attachment.row_id = data['row_id']
        attachment.table_name = self.dbh.table_name()
        attachment.is_public = data['is_public'] if 'is_public' in data else True

        self.gdb.add(attachment)
        self.gdb.flush()

        return attachment.attachment_id

    def AttachFileByUrl(self, url):
        from cg_tornado.models import UserFile
        query = self.gdb.query(UserFile).filter(UserFile.user_id == self.User.user_id).filter(UserFile.file_url == url)
        file = query.one_or_none()
        file.is_attached = True
        return

    def DeattachFileByUrl(self, url):
        from cg_tornado.models import UserFile
        query = self.gdb.query(UserFile).filter(UserFile.user_id == self.User.user_id).filter(UserFile.file_url == url)
        file = query.one_or_none()
        if file is not None:
            file.is_attached = False
        return

    # Common Controller Methods
    def List(self):
        columns = self.Data['columns'] if 'columns' in self.Data else []
        wheres = self.Data['where'] if 'where' in self.Data else {}
        orders = self.Data['order'] if 'order' in self.Data else []
        limit = self.Data['limit'] if 'limit' in self.Data else None
        offset = self.Data['offset'] if 'offset' in self.Data else None
        searchKey = self.Data['search'] if 'search' in self.Data and self.Data['search'] != '' else None

        columns, data, total = self.dbh.getList(columns=columns, wheres=wheres, orders=orders, limit=limit, offset=offset, searchKey=searchKey)

        resp = {
            'data': data,
            'total_records': total,
            'columns': columns
        }
        return resp

    def Single(self):
        if 'oid' not in self.Data:
            raise RequiredFieldMissing('oid')

        data = None
        if 'columns' in self.Data:
            data = self.dbh.getSingleForColumns(self.Data['oid'], self.Data['columns'])
        else:
            data = self.dbh.getSingle(self.Data['oid'])

        if data is not None:
            if 'sections' in self.Data:
                sections = self.Data['sections']
                for refCol in sections:
                    table = sections[refCol]['table']
                    columns = sections[refCol]['columns']
                    ctrl = self._loadController(table)
                    ctrl.Data = {'oid': data[ctrl.dbh.PrimaryKey], 'columns': columns}
                    rec = ctrl.Single()
                    if rec is not None:
                        for k in rec:
                            data[k] = rec[k]

            if 'foreign_keys' in self.Data:
                sections = self.Data['foreign_keys']
                for refCol in sections:
                    f_section = sections[refCol]
                    data_sub = {'columns': f_section['columns'], 'where': {'column': f_section['foreign_column'], 'search': data[refCol]}}
                    ctrl = self._loadController(f_section['table'], data_sub)
                    dataKey = '{0}_data'.format(refCol)
                    data[dataKey] = ctrl.LoadSelectOptions()

        if 'child' in self.Data:
            child = self.Data['child']
            # Check this
            # ctrl = self._loadController(child['slug'])
            # where = {'column': child['foreign_key'], 'search': self.Data['oid']}
            # cols, records, count = ctrl.getList(columns=[], wheres=where)
            # items = []
            # for row in records:
            #     items.append(model.getSingleForColumns(row[model.PrimaryKey], child['columns']))
            #
            # data['child_records'] = items

        return data

    def Create(self):
        if 'sections' in self.Data and self.Data['sections'] is not None:
            sections = self.Data['sections']
            for refCol in sections:
                table = sections[refCol]['table']
                data = sections[refCol]['data']
                ctrl = self._loadController(table, data=data)
                _id = ctrl.Create()
                self.Data[refCol] = _id

        row_id = self.dbh.insertRecord(self.Data)

        if 'attachments' in self.Data and isinstance(self.Data['attachments'], list):
            for attachment in self.Data['attachments']:
                attachment['row_id'] = row_id
                self._attachFile(attachment)

        return row_id

    def Update(self):
        self.AssertData(self.dbh.PrimaryKey)

        if 'sections' in self.Data and self.Data['sections'] is not None:
            sections = self.Data['sections']
            for refCol in sections:
                table = sections[refCol]['table']
                data = sections[refCol]['data']

                ctrl = self._loadController(table, data=data)
                data[refCol] = self.Data[ctrl.dbh.PrimaryKey]
                self.Data[refCol] = ctrl.Update()

        row_id = self.dbh.updateRecord(self.Data)
        return row_id

    def Attach(self):
        self.AssertData('file_id', 'row_id')
        row_id = self._attachFile(self.Data)
        return row_id

    def Delete(self):
        self.AssertData('oid')

        try:
            self.dbh.deleteRecord(self.Data['oid'])
        except IntegrityError:
            raise ChildRecordExists()

        return self.Data['oid']

    def FilterOptions(self):
        self.AssertData('column')

        columns = [self.Data['column']]
        searchKey = self.Data['search'] if 'search' in self.Data and self.Data['search'] != '' else None
        self.addTopWhere(columns[0], None, 'ne')

        wheres = self.Data['where'] if 'where' in self.Data else {}
        orders = self.Data['order'] if 'order' in self.Data else [{"column": "{}".format(columns[0]), "dir": "asc"}]

        columns, values, total = self.dbh.getList(columns=columns, wheres=wheres, orders=orders, limit=25, searchKey=searchKey, distinct=True, linear=True, noCount=True)

        data = [{'value': v[0]} for v in values]

        return data

    def LoadSelectOptions(self):
        columns = self.dbh.getDropdownColumns()
        primaryKey = self.dbh.PrimaryKey

        if 'columns' in self.Data and len(self.Data['columns']) > 0:
            columns = self.Data['columns']

        if primaryKey not in columns:
            columns.append(primaryKey)

        orders = self.Data['order'] if 'order' in self.Data else [{"column": "{}".format(columns[0]), "dir": "asc"}]
        searchKey = self.Data['search'] if 'search' in self.Data and self.Data['search'] != '' else None
        wheres = self.Data['where'] if 'where' in self.Data else {}

        cols, data, total = self.dbh.getList(columns=columns, wheres=wheres, orders=orders, limit=25,
                                             searchKey=searchKey, noCount=True)

        for obj in data:
            obj['value'] = obj[columns[0]]
            obj['id'] = obj[self.dbh.PrimaryKey]

        return data

    def SelectOptions(self):
        self.AssertData('slug')

        ctrl = self._loadController(self.Data['slug'], self.Data)
        return ctrl.LoadSelectOptions()
