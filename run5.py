from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(880, 400 ,0, False)
drive_general(100, 320 ,0, False)
drive_general(160, -70 ,0, False)

#do mission 8
drive_general(130, -80 ,0, False)

turn_general(-90)
drive_general(100, -450, -90, True)
turn_general(-55)
drive_general(130, -300, -55, True)

#put the ship in her place
drive_general(250, -360, -55, True)

drive_general(270, 200, -55, True)  
turn_general(40)
drive_general(70, 200, 40, True)
turn_general(40)
drive_general(70, -200, 40, True)
drive_general(200, 200, 40, True)
turn_general(75)
drive_general(250, 400, 75, True)
turn_general(15)

#go back home
drive_general(750, 1000, 15, True)
