from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(120, 300, 0, False)
turn_general(93)

#go backward to mission 3
drive_general(800, -350, 93, True)

#put the scubadiver on the yellow line and click on the yellow
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -365, Stop.BRAKE, True)
drive_general(300, 550, 93, True)
turn_general(-90)

#drive straight to mission 6
drive_general(80, 150, -90, True)

#get up the toren
drive_general(130, 70, -90, True)

#take the srimp
right_arm_motor.run_angle(400, 450, Stop.BRAKE, True)

#take the chest
drive_general(100, -200, -90, True)
turn_general(120)
drive_general(440, 700, 120, True)
