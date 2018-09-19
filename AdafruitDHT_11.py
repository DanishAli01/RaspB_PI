#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import requests
import json

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    # humidity = 39
    # temperature = 25
    data = {'humidity':humidity,'temperature':temperature}

    r = requests.get('http://127.0.0.1:5000/api/post_reading?temperature=' + str(temperature) + '&humidity=' + str(humidity))

    print(humidity,temperature)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    time.sleep(5)
