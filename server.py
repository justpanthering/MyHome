from flask import Flask
from flask_restful import Api, Resource

from api.sensors.DHT11_Temp_Humid import dht11_temp_humid

app = Flask(__name__)
app.register_blueprint(dht11_temp_humid)

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
