### Pet Dispenser 1.0.2
# Author: Yaron Kachalon
# Date: 2022-08-30

# -------------------------------------------
# This app launches a Discord bot that listens to certain keywords and activates a servo motor on an Arduino
# device that releases a treat for your pet. Tested on Ubuntu 20.04 with Pycharm and Arduino Uno.
# -------------------------------------------

# Arduino Control:
# Must change permissions on Arduino port so that this program can access it: sudo chmod 666 /dev/ttyACM0

from pyfirmata import Arduino, SERVO
from time import sleep

port = '/dev/ttyACM0'  # Port may be different on your setup (depending on OS). Use the official Arduino IDE to find it.
pin = 9               # The physical pin # on the Arduino in which the servo motor is connected to.
board = Arduino(port)  # Initialize the board.

board.digital[pin].mode = SERVO


def rotateServo(pin_num: int, angle: int):
    """
    Spins the servo motor via the Arduino Uno unit.

    Parameters
    ----------
    pin_num - The number of the physical pin to which the motor is connected on the Arduino board.
    angle - The direction in which the motor will spin. 0 = counter-clockwise, 90 = stop, 180 = clockwise.
    """

    board.digital[pin_num].write(angle)
    sleep(0.015)


rotateServo(pin, 90)  # Keeps the servo motor off.


# Discord Bot & Control:
# Must have a Discord user account and create a new application bot to get an API key.
# Reference: https://discord.com/developers/applications
# Once the bot is created and an API key obtained, invite the bot to your Discord server before running this app.

import discord

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)    # Initializes the bot.


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # If we write the word "treat" in the chat in Discord, this function will run:
    if message.content.startswith('treat') or message.content.startswith('Treat'):
        for i in range(0, 90):
            rotateServo(pin, i)
        await message.channel.send('Sent a treat to your pet!')


client.run('xxxxxxxxx')    # The bot's API key
