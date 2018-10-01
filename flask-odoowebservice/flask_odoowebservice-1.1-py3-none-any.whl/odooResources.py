from flask_restful import Resource,Api
from flask import request,jsonify,make_response
from .webService import OdooWebServiceClient
from ast import literal_eval
from base64 import b64decode
from flask_jwt_extended import create_access_token,\
jwt_refresh_token_required,jwt_required,get_jwt_identity,get_jwt_claims,JWTManager
from .database import UsersCollection


OdooApi = Api()
JWT = JWTManager()

class OdooWebServiceResources(OdooWebServiceClient):
    def init_app(self,app):
        if app != None:
            self.app = app
        JWT.init_app(app)
        OdooWebServiceClient.init_app(self,app)
    def add_resource(self,obj,route):
        OdooApi.add_resource(obj,route)

    def init_routes(self):
        OdooApi.init_app(self.app)

webClient = OdooWebServiceResources()

@JWT.user_identity_loader
def user_identity_lookup(username):
    user_collection = UsersCollection()
    _user = user_collection.find_one({'name':username})
    credential = {'uid':_user['uid'],'password':_user['password']}
    return credential

class OdooBaseResource(Resource):
    decorators = [jwt_required]
    module = None
    fields = ['name']
    domain = [[]]
    offsets = None
    limit = None

    def set_domain(self):
        if 'domain' in request.args:
            self.domain = literal_eval(request.args.get('domain'))

    def invalid_url(self):
        return jsonify(error='invalid url')

class OdooListResource(OdooBaseResource):

    def get(self,module=None,pk=None):
        if module and pk:
            return self.retrieve(module,pk)
        elif module:
           return self.list(module)
        else:
            return self.invalid_url(),400

    def list(self,module):
        self.set_domain()
        credential = get_jwt_identity()
        uid,password = credential['uid'],credential['password']
        response = webClient.search_read(uid=uid,password=password,module=module,\
                        domain=self.domain,fields=self.fields)

        data = jsonify(data=response)
        return make_response(data,200)

class OdooRetrieveResource(OdooListResource):
    def retrieve(self,module,pk):
        credential = get_jwt_identity()
        uid, password = credential['uid'], credential['password']
        response = webClient.browse(uid,password,module,pk)
        return jsonify(data=response)

class OdooDeleteResource(OdooBaseResource):
    def delete(self,module=None,pk=None):
        if module == None or pk == None:
            return self.invalid_url(),400
        credential = get_jwt_identity()
        uid, password = credential['uid'], credential['password']
        response = webClient.unlink(uid,password,module,pk)
        return jsonify(data=response)

class OdooAttributes(Resource):
    def get(self,module):
        credential = get_jwt_identity()
        uid, password = credential['uid'], credential['password']
        response = webClient.get_attribute(uid,password,module)
        return jsonify(data=response)

class OdooAuthResource(Resource):

    def _insert_user(self,username,uid,password):
        user_collection = UsersCollection()
        if user_collection.exists({'uid': uid}):
            doc = user_collection.find_one_and_update({'name':username},{'$set':{'uid':uid}})
            return doc
        return user_collection.insert({'name': username, 'uid': uid,'password':password})

    def post(self):
        if request.authorization != None:
            auth = request.authorization
            username,password = auth.get('username'),auth.get('password')
            uid = webClient.get_uid(username,password)
            if uid != None:
                self._insert_user(username,uid,password)
                return jsonify(access_token=create_access_token(username))
            return jsonify(error='Invalid credential')
        elif request.args['Authorization'] != None:
            type,token = request.args['Authorization'].split(None,1)
            username,password = b64decode(token).split(':',1)
            uid = webClient.get_uid(username, password)
            if uid != None:
                self._insert_user(username, uid, password)
                token = create_access_token(username)
                return jsonify(access_token=token)
            return jsonify(error='Invalid credential')
        else:
            return jsonify(error='Invalid credential')

