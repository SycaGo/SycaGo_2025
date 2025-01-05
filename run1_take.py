from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(200, 450)
turn_general(38)
drive_general(500, 450)
turn_general(27)
drive_general(250, 450)
right_arm_motor.run_angle(300, 400, Stop.BRAKE, True)
turn_general(-65)
drive_general(30, 350)
right_arm_motor.run_angle(200, -400, Stop.BRAKE, True)
right_arm_motor.run_angle(200, 400, Stop.BRAKE, True)
turn_general(30)
