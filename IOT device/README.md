# IoT Device

## Building the device
### Requirements
1. Raspberry Pi 4 Computer Model B 4GB RAM
2. GrovePi+
3. Pi Camera
4. Grove - Temperature and Humidity Sensor
5. Grove - Light Sensor
6. Grove - Sound Sensor

### Connections
1. Connect Pi camera to the camera module port in raspberry Pi (<i>refer</i> - https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
2. Connect GrovePi+ to the raspberry Pi (<i>refer</i> - https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/#:~:text=(note%3A%20if%20you%20don',will%20turn%20on%20the%20GrovePi.)
3. Connect temperature and humidity sensor to port D7 in grovepi+.
4. Connect sound sensor to port A0 in grovepi+.
5. Connect light sensor to port A1 in grovepi+.

After making the connections, the device will look like
![image](https://drive.google.com/uc?export=view&id=1NaRAIrBsq5L3t7OW54lPqOfULCWkHwwg)

## Installation
Onto the ceiling, close to the room door, with the camera facing the region where people have to cross through for entering and exiting a room

## Code Information
### light.py, sound.py, tempHum.py
These files contain the code to gather sensor readings(light, sound, temperature and humidity) from the environment.

### dataserver.py
This file is made as a local server to fetch the sensor values from camera and the rest of the sensors. The program then joins the data from both files and sends further to the server. This file ideally should be remote but for the demo purpose it is situated locally.

### combine.py
This file includes modules that read the values from temperature-humidity sensor, light sensor, and sound sensor. Combines all the values and sends to the dataserver.py.

### cameraCodeVideo.py
Reading the recorded video and processing the count of people inside the room (by calculating the number of people who have entered and exited) is done in this file. Further this count will be passed to the dataserver.py. 

### cameraCodeLiveStream.py
Reading the livestream video and processing the count of people inside the room (by calculating the number of people who have entered and exited) is done in this file. Further this count will be passed to the dataserver.py.

### Required packages
cv2, imutils, math, request, json, numpy, threading, picamera, statistics, grovepi, flask.

## Video Information
### video.mp4 
This is used by cameraCodeVideo.py as input

### preprocessed.mp4
This is recorded during the execution of cameraCodeVideo.py. This is preprocessed version of video.mp4.

### outputVideo.mp4
This is recorded during the execution of cameraCodeVideo.py. By watching this video one can understand how this code works

## Program execution
### Executing the code for recorded video input
1. Open the directory terminal.
2. Run command: <code><i>./StartProgrammeVideo.sh</i></code>

This will run three files 'dataserver.py', 'combine.py', and 'cameraCodeVideo.py'. 

### Executing the code for livestream video input
1. Open the directory terminal.
2. Run command: <code><i>./StartProgrammeLiveStream.sh</i></code>

This will run three files 'dataserver.py', 'combine.py', and 'cameraCodeLiveStream.py'.

Note: If bash files are not working, run the 3 python files for each category mentioned above in order

## Sample Output for capturing live occupancy in a room
<img src="https://media.giphy.com/media/nhZtxM3vwuRgpcAQAI/giphy.gif" alt="People count" width="100%">



