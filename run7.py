from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_alligment import line_alignment
drive_general(200,400, 0, False)
turn_general(-90)
drive_general(500,400, -90, True)
turn_general(-95)
drive_general(420,200, -95, True)
drive_general(10,-300, -95, True)
drive_general(100,200, -95, True)
drive_general(80,-100, -95, True)
turn_general(-95)
drive_general(600,550, -95, True)
