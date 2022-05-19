# Parking-Spot Finder

This project was to identify the available parking spots in a parking lot thereby indicating a driver
before entering the parking lot. For this project we used raspbery-py kit and databse (mysql-workbench). The park.py file contains sensor code and main.py file will upload the data recorded from the sensor into database. We fetch the recorded data from the database and visualize the data to analyze the parking spaces and it's status over a different time. 

# The Problem
In the modern day, the advancement of technology in the field of mobility has put
multiple forms of transport on the road. With the ever increasing transport sector, the
need for real estate to accommodate the vehicles when not in action is at a rise.
Parking lots in buildings and on roads are usually always found to be
accommodating and really hard to identify vacant spots in case of private vehicles.
Modern day car users face this challenge on an everyday basis, trying hard to find a
vacant spot before running into work or into a supermarket. This brought about the
challenge to identify and indicate the available parking spots to the driver in hand,
based on which the driver can make his way into the parking lot.

# Proposed Approach
The availability of a parking spot is entirely dependent on the presence of a car in the
parking lot. Identifying a car’s position in the parking spot helps provide an insight
into the availability of the slots in a particular building of parking spaces. For this
purpose, multiple methods can be incorporated but upon considering various
parameters and finalising upon the Ultrasonic sensor: HC- SR04.
Based on the flowchart above, a sequence can be derived for the workflow. As
indicated in the flowchart, the HC- SR04 collects data regarding the presence of a
car. This can be determined by the distance of the object determined by the HCSR04 sensor and based on the distance measured, the presence of a car can be
identified. Based on this principle, the detection of a car can be identified.

# Methods used in source code:
MySQL is used as the db management system. The Ultrasonic sensor sends
pulse signals and receives back if the signal is reflected. If the distance satisfies the
‘if’ condition, appropriate responses are recorded and saved in the database table.
We use grafana to visualize the received data.
We have assigned availability of parking spot as 1 and absence as 0 (boolean type
notation). Since we need to have live status of the availability of the parking spot, we
monitor continuously and gather every data from the sensor. This way we can use
grafana to not only determine the presence or absence of the parking spot, but also
to know how long the parking spot was occupied. This is an extension of the initial
application for cost estimation.

To run the sensor, you have to run main.py file. 
