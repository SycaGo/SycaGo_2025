from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(150, 350, True)

turn_general(40, 350, True)

drive_general(270, 350, True)

turn_general(-46, 275, True)

drive_general(130, 300, True)

turn_general(22, 100, True)

drive_general(190, 300, True)

turn_general(-20, 100, True)

drive_general(280, 350, True)

drive_general(-450, 300, True)

turn_general(24, 275, True)

drive_general(290, 300, True)

turn_general(60, 275, True)

drive_general(300, 300, True)

turn_general(30, 275, True)

drive_general(200, 300, True)

turn_general(-30, 275, True)

#left_arm_motor.run_angle(300, -50, Stop.BRAKE, True)
