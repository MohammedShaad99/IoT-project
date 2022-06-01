from grovepi import *
light_sensor = 1 # Connect the sensor to A1.

def get_light_intensity():
    try:
        light_sensor_value = analogRead(light_sensor)
        return light_sensor_value
    except (IOError):
        print("Error")
