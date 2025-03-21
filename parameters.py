from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.robotics import DriveBase

hub = PrimeHub()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

WHEEL_DIAMETER = 62.4
AXLE_TRACK = 110
drive_base = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)
drive_base.use_gyro(True)

# left/right_arm_motor.run_angle(speed_deg/s, rotation_angle_deg, Stop.BRAKE, wait(bool))
left_arm_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_arm_motor = Motor(Port.C)

right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)
