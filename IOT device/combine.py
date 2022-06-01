import json
from time import sleep
import requests
from math import isnan
import statistics as stats
from sound import * 
from temp import * 
from light import *
import threading
import numpy as np

url = "http://127.0.0.1:5000/webhook"
prev_temp = 23.0
current_temp = 0.0
prev_humidity = 45.0
current_humidity = 0.0

def sendSensorData(temp,humidity,light,sound):
    data = [{'sensor': 10},{"temp":temp, 'humidity':humidity, 'light':light,'sound':sound}]
    requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

while True:
    try:
        temp, humidity = get_temp()
        if isnan(temp):
            current_temp = prev_temp
        else:
            current_temp = temp
            prev_temp = temp
        
        if isnan(humidity):
            current_hum = prev_humidity
        else:
            current_hum = humidity
            prev_humidity = humidity
        
        light = get_light_intensity()
        sound = get_sound()
        
        t = threading.Thread(target=sendSensorData,args = (current_temp,current_hum,light,sound,))
        t.setDaemon(True)
        t.start()
            
    except IOError:
        print("Error")

