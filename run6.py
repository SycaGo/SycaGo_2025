from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_aligment import line_alignment
#octupos
drive_general(420, 400)

#take shrimps and coral
drive_general(200, -400)
left_arm_motor.run_angle(-300, 300, Stop.BRAKE, True)
turn_general(42)
drive_general(530, 400)

#mission 13
turn_general(-30)
drive_general(40, -400)
left_arm_motor.run_angle(200, 295, Stop.BRAKE, True)
drive_general(50, -400)
left_arm_motor.run_angle(200,-295, Stop.BRAKE, True)
drive_general(70, 400)

'''
turn_general(40)
drive_general(80, 400)
'''
