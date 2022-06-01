# Find my room

<p>
The project is divided into two parts IoT implementation and Web application.
Motive of this project is to create an application for users, that can provide which room they want to go to depending on their preferences of how their room should be - like atmosphere inside a particular room (Temperature, Humidity, Sound, Light) and live occupancy. 
</p>

# IoT Implementation
<p>
The solution is tailored around raspberry pi but can be expanded to other devices if need be. Taking input from camera module, raspberry pi uses pixel calculation, for comparing each frame with the previous frame to detect any activity. This helps in determing the number of people who have entered and exited, thereby calculating the live occupancy. Moreover, temperature-humidity sensor, sound sensor and light sensor will keep on sensing the values and raspberry pi processes them to the understandable standards and sends the live occupancy count along with sensor values to the web application using flask server.

For more information
</p>

# Web Application 
<p>
This server is a passive component and a three-layer architecture that has a web application, database, admin-flask, and website. The server contains a database used for storing the user information, logs containing the webhooks coming from the local server, and a table for keeping the room value. Google data studio is implemented on the database which provides an analysis report on the information inside it. For the admin dashboard, admin-flask is being used in the cloud server to manage records in the databases. Moreover, there is a machine learning model being used for identifying abnormal conditions, and in case of one mail will be sent to the appropriate person. Furthermore, the cloud server also hosts a website and the URL is https://iotuni.herokuapp.com/. This web application displayed the temperature, noise, humidity, light, and occupancy of the room which are stored in the database. Also, users could register themself and with the same registered credentials, the user could log in and choose the desired room based.</p>


   
