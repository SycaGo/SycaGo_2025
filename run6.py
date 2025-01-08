from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_aligment import line_alignment
#octupos
drive_general(420, 400, 0, False)

#take shrimps and coral
drive_general(200, -400, 0, False)
left_arm_motor.run_angle(-300, 300, Stop.BRAKE, True)
turn_general(42)
drive_general(530, 400, 42, True)

#mission 13
turn_general(-30)
drive_general(40, -400, -30, True)
left_arm_motor.run_angle(200, 295, Stop.BRAKE, True)
drive_general(50, -400, -30, True)
left_arm_motor.run_angle(200,-295, Stop.BRAKE, True)
drive_general(70, 400, -30, True)
