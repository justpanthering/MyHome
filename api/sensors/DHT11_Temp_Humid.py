from flask import Blueprint, abort
from flask_restful import Api, Resource

import board
import adafruit_dht

dht11_temp_humid = Blueprint('dht11_temp_humid', __name__)
api = Api(dht11_temp_humid)


dht = adafruit_dht.DHT11(board.D2)

class Readings(Resource):
    def get(self):
        try:
            temperature = dht.temperature
            humidity = dht.humidity
            return {
                    'temperature': temperature,
                    'humidity': humidity
                    }
        except RuntimeError as e:
            abort(500)

api.add_resource(Readings, '/sensors/dht11')
