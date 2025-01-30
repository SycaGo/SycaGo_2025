from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(640, 500, 0, False)
turn_general(24)
right_arm_motor.run_angle(300, 330, Stop.BRAKE, False)
drive_general(300, 450, 24, True)
turn_general(120, False)
drive_general(40, 200, 120, True)
left_arm_motor.run_angle(600, 280, Stop.BRAKE, True)
drive_general(100, -400, 120, True)
left_arm_motor.run_angle(300, -250, Stop.BRAKE, True)
drive_general(50, 200, 0, False)
turn_general(70)
drive_general(250, 500, 70, True)
turn_general(-35, False)
drive_general(660, 1000, -35, True)
