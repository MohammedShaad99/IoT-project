from grovepi import *
import numpy as np
soundSensor = 0 # Connect sound sensor to A0.

def get_sound():
    try:
        soundSensorValue = analogRead(soundSensor)
        decibelSound = int(20*np.log10(soundSensorValue))
        return decibelSound
    
    except (IOError):
        print("Error")
