from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(150, 300, True)

turn_general(32, 275, True)

drive_general(230, 300, True)

turn_general(-50, 275, True)

drive_general(150, 300, True)

turn_general(25, 275, True)

drive_general(170, 300, True)

drive_general(-270, 300, True)

turn_general(25, 275, True)

drive_general(370, 300, True)

drive_general(-800, 300, True)
