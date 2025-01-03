from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_aligment import line_alignment

#mission 9
drive_general(130, 400)
turn_general(-27)
drive_general(400,400)
turn_general(-20)
drive_general(150,400)
turn_general(-20)
line_alignment(500)
turn_general(-60)
right_arm_motor.run_angle(-10000, 1500, Stop.BRAKE, True)
turn_general(-10)
drive_general(80, 400)
turn_general(10)


