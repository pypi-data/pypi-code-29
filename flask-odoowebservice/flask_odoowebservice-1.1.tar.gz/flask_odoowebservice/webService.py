from flask import current_app
from xmlrpc.client import ServerProxy



class OdooWebServiceClient(object):
    def __init__(self,app=None):
        self.app = app
        if self.app:
            self.init_app(self.app)

    def search(self,uid,password,module,fields={}):
        models = self.get_model()
        return models.execute_kw(current_app.config['ODOO_DB'],uid,\
        password,module, 'search_read',[[]],fields)

    def browse(self,uid,password,module,_id,fields={}):
        models = self.get_model()
        return models.execute_kw(current_app.config['ODOO_DB'], uid, password,
                          module, 'read',[_id],{'fields':fields})

    def get_attribute(self,uid,password,module):
        model = self.get_model()
        return model.execute_kw(current_app.config['ODOO_DB'], uid, password,\
        module, 'fields_get',
        [], {'attributes': ['type']})

    def unlink(self,uid,password,module,_id):
        models = self.get_model()
        return models.execute_kw(current_app.config['ODOO_DB'], uid, password,\
        module, 'unlink', [_id])

    def search_read(self,uid,password,module,domain,fields):
        models = self.get_model()
        return models.execute_kw(current_app.config['ODOO_DB'],uid,\
        password,module, 'search_read',domain,{'fields':fields})

    def get_common(self):
        return ServerProxy('{}/xmlrpc/2/common'.format(self.url))

    def get_uid(self,username,password):
        common = self.get_common()
        db = current_app.config['ODOO_DB']
        uid = common.authenticate(db,username,password,{})
        return uid

    def get_model(self):
        model = ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        return model

    def init_app(self,app):
        app.config.setdefault('ODOO_URL','http://localhost')
        app.config.setdefault('ODOO_PORT', '8069')
        app.config.setdefault('ODOO_DB', 'odoo8db')
        self.url = app.config['ODOO_URL'] + ':' + app.config['ODOO_PORT']