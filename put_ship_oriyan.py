from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(400, 500 ,0, False)
drive_general(400, 380 ,0, False)
drive_general(140, 320 ,0, False)
drive_general(100, -80 ,0, False)

#do mission 8
drive_general(140, -60 ,0, False)
turn_general(-90)
drive_general(100, -450, -90, True)
turn_general(-60)

#put the ship in her place
drive_general(320, -550, -60, True)
drive_general(270, 500, -60, True)  
turn_general(60)
drive_general(70, 300, 60, True)
turn_general(70)
drive_general(200, 200, 70, True)
turn_general(15)
drive_general(250, 400, 15, True)
turn_general(40)

#go back home
drive_general(700, 1000, 40, True)
