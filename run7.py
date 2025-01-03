from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_alligment import line_alignment

#mission 9
drive_general(130, 400)
turn_general(-30)
drive_general(400,400)
turn_general(-20)
drive_general(150,400)
turn_general(-15)
line_alignment(350)
