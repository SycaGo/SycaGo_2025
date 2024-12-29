from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take first coral
drive_general(150, 350)

turn_general(40)

drive_general(220, 350)

#take second coral
turn_general(-48)

drive_general(130, 300)

#take first shrimp
turn_general(18)

drive_general(170, 300)

#Alignment on a wall
turn_general(-12)

drive_general(300, 350)

#take first water sample
drive_general(450, -300)

turn_general(20)

drive_general(280, 300)

#take second water sample
turn_general(30)

drive_general(200, 300)

turn_general(40)

drive_general(280, 300)

turn_general(-30)

drive_general(50, 300)

right_arm_motor.run_angle(15000, 2000, Stop.BRAKE, True )
