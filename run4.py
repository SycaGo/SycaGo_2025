from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(60, 200 ,0, False)
turn_general(90)

#do mission 8
drive_general(780, 400 ,90, True)
drive_general(70, 320 ,90, True)
drive_general(100, -200 ,90, True)
drive_general(100, -30 ,90, True)
drive_general(20, -200 ,90, True)
turn_general(-60)
drive_general(60, 300 ,-60, True)
turn_general(-17)
drive_general(200, -1000 ,-17, True)
drive_general(10, 500 ,-17, True)
turn_general(-74)
wait(200)
drive_general(150, -200 ,0, False)
turn_general(-5)
drive_general(150, -200 ,0, False)
drive_general(50, 200 ,0, False)



'''
turn_general(-40)
drive_general(70, 200 ,-40, True)

#take the trident out
turn_general(-45)

#back to the wall
drive_general(200, -2000 ,-45, True)

#put the ship in her place
turn_general(-55)
drive_general(100, -250, 0, False)
turn_general(-5)
drive_general(140, -350, 0, False )
drive_general(80, 350, 0, False )
'''
