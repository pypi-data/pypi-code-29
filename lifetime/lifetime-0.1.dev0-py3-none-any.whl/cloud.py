from flask import Flask, request
from flask_restful import Resource, Api
import json

# Message Dict
activities = {}

class HelloFlask(Resource):
    def get(self):
        return {'hello': 'flask'}

class Events(Resource):
    def get(self, user):
        if user in activities.keys():
            return activities[user]

    def put(self, user):
        if user not in activities.keys():
            activities[user] = []
        activities[user].append(request.json)
        print(request.json)

app = Flask(__name__)

def main():
    api = Api(app)
    api.add_resource(HelloFlask, '/')
    api.add_resource(Events, '/<string:user>')

    app.run(host='localhost', port=7777)

if __name__ == '__main__':
    main()
