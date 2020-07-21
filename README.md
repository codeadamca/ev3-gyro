# ev3-gyro
A Python snippet utilizing the LEGO EV3 gyro sensor, the LEGO EV3 Brick and [Pybricks](https://pybricks.com/). [Pybricks](https://pybricks.com/) is the LEGO recommended method of using the LEGO EV3 Brick with Python. See the official [Python for EV3](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3) LEGO page for more details. 

This example will change the speed and direction of a motor based on the angle of the gyro sensor.

Of all the EV3 sensors, the gyro sensor seems to cause the most problems. Here are some issues that I ran into:

## Calibration
The gyro sensors calibrates itself to determine what is zero for both speed and angle. The angle is reset at the beginning of the script using the reset_angle method. THe speed is reset when the sensor is plugged in. If the starting speed is not zero unplug the gyro sensor from the EV3 brick and then plug it back in, try not to move it when you plug it back in.

## Rotation
The rotation is based on the diagram on the EV3 gyro sensor. The red dot is the center of the rotation. Clockwise is positive and counter-clockwise is negative. However, this can be switched when initializing the gyro sensor. 

<a href="https://codeadam.ca">
<img src="https://codeadam.ca/images/code-block.png" width="100">
</a>
