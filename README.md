### Updates:
Version 1.0.4:
 - Changed treat function to accomodate new dispenser design. 
 - Added two new functions to rotate the dispenser fully right/left in case treats are stuck.

Version 1.0.2:
 - Adjusted servo motor function's timing and speed. 
 - Added comments and descriptions where needed. 
 
Version 1.0.0:
 - First stable version.


# Treats Dispenser:
A mini python app that connects to Discord and an Arduino device with a servo motor, 
allowing you to video chat with your pet and give it treats via chat command.

Tested and built on Ubuntu 20.04 and Arduino Uno.


## Concept: 
I always wanted to be able to see my cat and give it treats while I'm at work or travelling,
but all existing solutions on the market are really expensive (minimum $250). I decided to build
my own solution using an old laptop that is not in use and an Arduino unit with a motor. 

The laptop is on 24/7 and connected to my Discord server in video chat, which allows me to connect
to the same video chat room from my phone or another computer whenever I want, see my cat and write the word "treat"
in the chat to give it a treat!

Total cost of the solution: ~$50 for the Arduino unit and the motor + time and creativity for
building the treats container. 


### Requirements: 
- Two active Discord accounts - one for the on-prem laptop to stay connected to the video chat, and one for your personal use: www.discord.com 
- An Arduino Uno unit: https://www.arduino.cc/en/Guide/ArduinoUno
- A Servo motor unit: https://arduinogetstarted.com/tutorials/arduino-servo-motor


### How to build and deploy (very basic instructions without details for now):
1. Connect the Arduino unit to the computer. 
2. Find the used USB port's name/number using the official Arduino IDE app (from their official website).
3. Edit the 'port' variable in the python code accordingly.
4. In the official Arduino IDE app, select File -> Examples -> Firmata -> StandardFirmata, then upload that code to the Arduino.
5. Create a new developer app in Discord: https://discord.com/developers/applications
6. Create a bot and get an API key, then invite the bot into your Discord server/room.
7. Put the bot's API key in the last line of the code where the "xxxxxxx" part is.
8. Connect the servo motor to the Arduino unit as shown here: https://arduinogetstarted.com/images/tutorial/arduino-servo-motor-wiring-diagram.jpg
9. Run the code and test by writing the word "treat" in the discord chat. If all is well the motor shuld move and the bot will say it sent a treat!
10. Use your creativity to design/build a container for the treats that the motor will be connected to and act as a dispenser on command. 


### Known issues: 
- If you're using Linux/Mac, you might encounter a permission error stating the app doesn't have permissions to access the port.
I used "sudo chmod 666 /dev/ttyACM0" to make that port accessible by anyone and everyone - but that's a security risk so keep it in mind. 
This needs to be done after every restart and/or every time the Arduino is reconnected to the computer.

