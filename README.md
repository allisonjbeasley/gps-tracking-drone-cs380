# CS380 Final - Arduino-Tracking Drone

This project allows for a DJI Tello drone to follow a user holding an Arduino Uno. The Arduino is equipped with two buttons for takeoff/landing (white button) and tracking/stationary (blue button) settings. The Arduino collects location information using GPS, and subsequently sends movement data to the python program via XBee. The python program interpets this data and sends commands to the Tello drone via wifi. The web app was seperated for the purpose of our demo, and creates an application that displays GPS data on a map. This data can be manipulated in the python program. 

## Required libraries/versions

Requires python3, Arduino IDE.
If digi-xbee library not already installed, enter 'pip install digi-xbee'
Must install Flask library. 

## Environment setup

- Make sure code from Final.ino is uploaded to the Arduino Uno while the XBee   layer is switched into dline. 
- Switch the Arduino into uart on the XBee layer. Make sure the GPS layer is switched to sw-uart.
- Once the Arduino is connected successfully, turn on drone and connect computer to correct Tello wifi network
- Start the python program Tello3.py and begin usage
- For convenience, the batter pack can be used so the Arduino can be moved independantly from a computer. Make sure the code is uploaded beforehand and that computer is still in range of XBee. 
- For the web app, run app.py and follow the link provided by output to see application

## Usage

- Press the white button to make the drone takeoff and land
- If the drone is currently flying, press the blue button to toggle between "tracking" mode and "stationary" mode. The drone is initially set in "stationary" mode each time it takes off.
- If the drone is in "tracking" mode, it will follow the user's movements based on GPS data. 
- If the drone is in "stationary" mode, it will stop moving and only hover 

## Contributors

Bobby Scott & Allison Beasley
