# LEGO® Mindstorms® EV3 and the Gyro Sensor

A Python snippet utilizing the LEGO EV3 gyro sensor, the LEGO EV3 Brick and [Pybricks](https://pybricks.com/). [Pybricks](https://pybricks.com/) is the LEGO recommended method of using the LEGO EV3 Brick with Python. See the official [Python for EV3](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3) LEGO page for more details. 

This example will change the speed and direction of a motor based on the angle of the gyro sensor.

> The documentation for Pybricks is really helpful:  
> [https://docs.pybricks.com/en/latest/ev3devices.html](https://docs.pybricks.com/en/latest/ev3devices.html)

Of all the EV3 sensors, the gyro sensor seems to cause the most problems. Here are some issues that I ran into:

## Speed Calibration
The gyro sensors calibrates the starting speed when the sensor is plugged into the EV3 brick. If the starting speed is not zero, unplug the gyro sensor from the EV3 brick and then plug it back in. Keep the gyro sensor still when you plug it in to give it a chance to callibrate.

## Angle Calibration
The gyro sensors calibrates the starting angle when the sensor is plugged into the EV3 brick. However, the angle can be reset using the reset_angle method. In this script the angle is reset chortly after the beep. Make sure the sensor is positioned at zero when you start the script.

## Rotation
The rotation is based on the diagram on the EV3 gyro sensor. The red dot is the center of the rotation. Clockwise is positive and counter-clockwise is negative. If desired, this can be switched when initializing the gyro sensor. 

---

## Repo Resources

- [Pybricks](https://pybricks.com/)
- [Python for EV3](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)

<a href="https://codeadam.ca">
<img src="https://codeadam.ca/images/code-block.png" width="100">
</a>

