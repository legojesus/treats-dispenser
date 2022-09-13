### Pet Dispenser 1.0.4
# Author: Yaron K.
# Date: 2022-09-13
# Git Repo: https://github.com/legojesus/treats-dispenser

# -------------------------------------------
# This app launches a Discord bot that listens to certain keywords and activates a servo motor on an Arduino
# device that releases a treat for your pet. Tested on Ubuntu 20.04 with Pycharm and Arduino Uno.
# -------------------------------------------

# Arduino Control:
# Must change permissions on Arduino port so that this program can access it: sudo chmod 666 /dev/ttyACM0

from pyfirmata import Arduino, SERVO
from time import sleep

port = '/dev/ttyACM0'  # Port may be different on your setup (depending on OS). Use the official Arduino IDE to find it.
pin = 9                # The physical pin # on the Arduino in which the servo motor is connected to.
board = Arduino(port)  # Initialize the board.

board.digital[pin].mode = SERVO


def rotate_servo(pin_num: int, angle: int):
    """
    Spins the servo motor via the Arduino Uno unit.

    Parameters
    ----------
    pin_num - The number of the physical pin to which the motor is connected on the Arduino board.
    angle - The direction in which the motor will spin. 0 = counter-clockwise, 90 = stop, 180 = clockwise.
    """

    board.digital[pin_num].write(angle)
    sleep(0.015)


def right_rotate():
    """
    Rotates the dispenser clockwise multiple times. Used if some treats are stuck in the dispenser.
    """

    for i in range(0, 90):
        rotate_servo(pin, i)
        rotate_servo(pin, i)
        rotate_servo(pin, i)
        rotate_servo(pin, i)


def left_rotate():
    """
    Rotates the dispenser counter-clockwise multiple times. Used if some treats are stuck in the dispenser.
    """

    for i in range(90, 180):
        rotate_servo(pin, i)
        rotate_servo(pin, i)
        rotate_servo(pin, i)
        rotate_servo(pin, i)

    rotate_servo(pin, 90)  # Stops the motor.


def give_treat():
    """
    Rotates the dispenser quickly to drop a few treats on command.
    """
    for i in range(0, 90):
        rotate_servo(pin, i)
    rotate_servo(pin, 90)  # Stops the motor.


rotate_servo(pin, 90)  # Sets the servo motor off on initialization.

# Discord Bot & Control:
# Must have a Discord user account and create a new application bot to get an API key.
# Reference: https://discord.com/developers/applications
# Once the bot is created and an API key obtained, invite the bot to your Discord server before running this app.

import discord

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)  # Initializes the bot.


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # If we write the word "treat" in the chat in Discord, this code will release a treat by opening and closing the
    # container using the servo motor:
    if message.content.startswith('treat') or message.content.startswith('Treat'):
        give_treat()
        await message.channel.send('Sent a treat to your pet!')

    # Rotates the dispenser clockwise multiple times in case some treats are stuck.
    if message.content.startswith('right') or message.content.startswith('Right'):
        right_rotate()
        await message.channel.send('Dispenser rotated successfully.')

    # Rotates the dispenser counter-clockwise multiple times in case some treats are stuck.
    if message.content.startswith('left') or message.content.startswith('Left'):
        left_rotate()
        await message.channel.send('Dispenser rotated successfully.')


if __name__ == "__main__":
    client.run('xxxxxxxxxx')    # The bot's API key
