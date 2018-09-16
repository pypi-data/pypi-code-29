from flask import Flask, request
from flask_restful import Resource, Api

# Message List
activities = {}

app = Flask(__name__)
api = Api(app)

class HelloFlask(Resource):
    def get(self):
        return {'hello': 'flask'}
api.add_resource(HelloFlask, '/')

import json
class Events(Resource):
    def get(self, user):
        if user in activities.keys():
            return activities[user]

    def put(self, user):
        if user not in activities.keys():
            activities[user] = []
        activities[user].append(request.json)
        print(request.json)

api.add_resource(Events, '/<string:user>')

if __name__ == '__main__':
    app.run(host='192.168.1.110', port=7777)

