from flask_mongokat import MongokatDocument,MongokatCollection

class UsersDocument(MongokatDocument):
    def get_name(self):
        return self["uid"]

class UsersCollection(MongokatCollection):
    document_class = UsersDocument
    col = 'userb'
    unique_fields = ['uid']
    structure = {
        'name':str,
        'uid':str,
        'password':str
    }





