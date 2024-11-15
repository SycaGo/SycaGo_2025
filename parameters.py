from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.robotics import DriveBase

hub = PrimeHub()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

WHEEL_DIAMETER = 62.4
AXLE_TRACK = 124
drive_base = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

left_arm_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_arm_motor = Motor(Port.C)

right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)
