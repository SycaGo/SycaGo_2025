from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take first coral
drive_general(150, 350, True)

turn_general(40, 350, True)

drive_general(270, 350, True)

#take second coral
turn_general(-46, 275, True)

drive_general(130, 300, True)

#take first shrimp
turn_general(22, 100, True)

drive_general(190, 300, True)

#Alignment on a wall
turn_general(-20, 100, True)

drive_general(280, 350, True)

#take first water sample
drive_general(-450, 300, True)

turn_general(27, 275, True)

drive_general(310, 300, True)


#take second water sample
turn_general(53, 275, True)

drive_general(350, 300, True)

turn_general(25, 275, True)

drive_general(50, 300, True)

turn_general(-16, 275, True)

drive_general(100, 300,True)
'''
#left_arm_motor.run_angle(300, -50, Stop.BRAKE, True)
'''
