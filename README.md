# Treats Dispenser:
A python app that connects to Discord and an Arduino device with a servo motor, 
allowing you to video chat with your pet and give it treats via chat command.

Tested and built on Ubuntu 20.04 and Arduino Uno.


## Concept: 
I always wanted to be able to see my cat and give it treats while I'm at work or travelling,
but all existing solutions on the market are really expensive (minimum $250). I decided to build
my own solution using an old laptop that is not in use and an Arduino unit with a motor. 

The laptop is on 24/7 and connected to my Discord server in video chat, which allows me to connect
to the same video chat room from my phone or another computer, see my cat and write the word "treat"
in the chat to give it a treat!

Total cost of the solution: ~$50 for the Arduino unit and the motor + time and creativity for
building the app and treats container. 


### Requirements: 
- An active Discord account: www.discord.com 
- An Arduino Uno unit: https://www.arduino.cc/en/Guide/ArduinoUno
- A Servo motor unit: https://arduinogetstarted.com/tutorials/arduino-servo-motor


### How to build and deploy:
1. Connect the Arduino unit to the computer. 
2. Find the used port's name/number using the official Arduino IDE app (from their official website).
3. Edit the port variable in the code accordingly.
4. Create a new app in Discord: https://discord.com/developers/applications
5. Create a bot and get an API key, then invite the bot into your Discord server/room.
6. Put the bot's API key in the last line of the code where the "xxxxxxx" part is.
7. Connect the servo motor to the Arduino unit as shown here: https://arduinogetstarted.com/images/tutorial/arduino-servo-motor-wiring-diagram.jpg
8. Run the code and test by writing the word "treat" in the discord chat. If all is well the motor shuld move and the bot will say it sent a treat!
9. Use your creativity to design/build a container for the treats that the motor will be connected to and act as a dispenser on command. 
