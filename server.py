from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class returnjson(Resource):
    def get(self):
        data = {
                "title": "Hello, World",
                "message": "This is a simple example to demonstrate the use of flask_restful",
                }
        return data

api.add_resource(returnjson, '/returnjson')

if(__name__=='__main__'):
    app.run(host='0.0.0.0', port=8123)
