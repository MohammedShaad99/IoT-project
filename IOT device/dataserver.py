from flask import Flask, request, abort
import requests
import json

app = Flask(__name__)
count=0
sensor = {"temp":23, 'humidity':45, 'light':40,'sound':45}
webhookUrl = 'https://iotuni.herokuapp.com/home'

def lightConvert(sensorData):
    return 'low' if sensorData <= 400 else 'medium' if sensorData > 400 and sensorData < 800 else 'high' 

def soundConvert(sensorData):
    return 'low' if sensorData <= 35 else'medium' if sensorData > 35 and sensorData < 50 else 'high'

def convertToStr(sensorData, sensorType):
    if sensorType == 'light':
        return lightConvert(sensorData)
    elif sensorType == 'sound':
        return soundConvert(sensorData)
    else:
        return -1
    
@app.route('/webhook', methods=['POST'])
def webhook():
    
    global count 
    global sensor

    if request.method == 'POST' and request.json[0].get('camera') :
        count = request.json[0]['camera']
        webhookdata = [{'room_id': 3,'liveCapacity':count,'temp':sensor['temp'],'sound':convertToStr(sensor['sound'], 'sound'),'humdity':sensor['humidity'],'light':convertToStr(sensor['light'], 'light')}]
        requests.post(webhookUrl, data=json.dumps(webhookdata), headers={'Content-Type': 'application/json'})
        return 'success', 200

    elif request.method == 'POST'  and request.json[0].get('sensor'):
        sensor = request.json[1]
        webhookdata = [{'room_id': 3,'liveCapacity':count,'temp':sensor['temp'],'sound':convertToStr(sensor['sound'], 'sound'),'humdity':sensor['humidity'],'light':convertToStr(sensor['light'], 'light')}]
        requests.post(webhookUrl, data=json.dumps(webhookdata), headers={'Content-Type': 'application/json'})
        return 'success', 200

    else:
        abort(400)
        
if __name__ == '__main__':
    app.run()