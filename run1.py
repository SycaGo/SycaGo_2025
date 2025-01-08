from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(200, 450, 0, False)
turn_general(36)
drive_general(460, 450, 36, True)
turn_general(27)
drive_general(280, 450, 27, True)
right_arm_motor.run_angle(300, 400, Stop.BRAKE, True)
turn_general(120)
left_arm_motor.run_angle(800, 215, Stop.BRAKE, True)
drive_general(70, -400, 120, True)
left_arm_motor.run_angle(800, -220, Stop.BRAKE, True)
drive_general(50, 300, 120, True)
turn_general(60)
drive_general(250, 600, 60, True)
turn_general(-30)
drive_general(600, 800, -30, True)
