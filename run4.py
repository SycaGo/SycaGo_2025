from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general
drive_general(40, 200 ,0, False)
turn_general(90)

#do mission 8
drive_general(800, 400 ,90, True)
drive_general(50, 320 ,90, True)
drive_general(200, -60 ,90, True)
drive_general(60, -200 ,90, True)
turn_general(-60)
drive_general(50, 200 ,-60, True)
turn_general(-90)
turn_general(20)
drive_general(130, -300, 0, False)

#put the ship in her place
drive_general(300, -360, 0, False)
drive_general(100, 400, 0, False)
