import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D2)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)
