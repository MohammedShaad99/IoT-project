from grovepi import *
sensorPort = 7 # connect the the temperature and humidity sensor to D7 port on grove pi.
sensorType = 0 # Depends on sensor the colour of a sensor. Blur = 0, White = 1.

def get_temp():
    try:
        [temperature, humidity] = dht(sensorPort,sensorType)
        return temperature, humidity
    except (IOError):
        print("Error")
        pass
