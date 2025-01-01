from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take first coral
drive_general(130, 400)

turn_general(40)

drive_general(280, 400)
drive_general(50, -400)

#take second coral
turn_general(-40)

drive_general(220, 400)
drive_general(50, -400)
#take first shrimp
turn_general(17)

drive_general(190, 350)

#Alignment on a wall
turn_general(-17)

drive_general(300, 330)

#take first water sample
drive_general(450, -500)

turn_general(20)

drive_general(250, 350)

#take second water sample
turn_general(28)

drive_general(200, 350)

turn_general(40)

drive_general(240, 350)

turn_general(-20)

drive_general(65, 300)

left_arm_motor.run_angle(300, -500, Stop.BRAKE, True )

#go back home
drive_general(150, -600)
turn_general(20)
drive_general(200, -600)
turn_general(70)
drive_general(400, 600)
