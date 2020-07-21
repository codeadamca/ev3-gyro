#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, GyroSensor)
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Initialize EV3 touch sensor and motors
motor = Motor(Port.A)
gyro = GyroSensor(Port.S1)

# Hold the gyro sensor still. THe program will display the current gyro
# speed. If the speed is not close to zero unplug the gyro sensor from the
# EV3 brick, hold it still and plug is back in.
print("Speed: ", gyro.speed())

# Create a loop to react to buttons
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        motor.stop()
        break

    # Rotate the gyro sensor using the red dot as the center. The angle will
    # range from -90 to 90. This is close to perfect as the motor dc method
    # requires a value from -100 to 100.
    motor.dc(gyro.angle())

    wait(10)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
