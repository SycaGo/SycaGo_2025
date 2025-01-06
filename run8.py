from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_aligment import line_alignment

#mission 9
drive_general(130, 400)
turn_general(-27)
drive_general(450,400)
turn_general(75)
drive_general(400,200)
drive_general(50,-400)
drive_general(200,200)

#mission 10
drive_general(280,-400)
turn_general(-100)
line_alignment(500)
turn_general(-50)
drive_general(50,400)
right_arm_motor.run_angle(-10000, 1700, Stop.BRAKE, True)
right_arm_motor.run_angle(10000, 1700, Stop.BRAKE, True)
'''
turn_general(-10)
drive_general(80, 400)
turn_general(15)
drive_general(50, 400)
#turn_general(10)
'''
