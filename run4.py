from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(60, 200 ,0, False)
turn_general(90)

#do mission 8
drive_general(780, 400 ,90, True)
drive_general(70, 400 ,90, True)
drive_general(100, -200 ,90, True)
drive_general(100, -30 ,90, True)
drive_general(20, -300 ,90, True)
turn_general(-60)
drive_general(180, 300 ,-60, True)
turn_general(40)
left_arm_motor.run_angle(1000, 300, Stop.BRAKE, True)

#get out the trident
drive_general(100, -400 ,40, True)
turn_general(-72)
