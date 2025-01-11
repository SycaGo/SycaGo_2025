from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(880, 400 ,0, False)
drive_general(50, 320 ,0, False)
drive_general(200, -60 ,0, False)

#do mission 8
drive_general(100, -80 ,0, False)

turn_general(-90)
drive_general(100, -450, -90, True)
turn_general(-65)
drive_general(130, -300, 0, False)

#put the ship in her place
drive_general(235, -360, 0, False)
drive_general(100, 400, 0, False)
