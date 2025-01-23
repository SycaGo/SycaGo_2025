from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(120, 300, 0, False)
turn_general(93)

#go backward to mission 3
drive_general(780, -350, 93, True)

#put the scubadiver on the yellow line and click on the yellow
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -365, Stop.BRAKE, True)
drive_general(350, 400, 0, False)
turn_general(-90)

#drive straight to mission 6
drive_general(85, 150, 0, False)

#get up the toren
drive_general(130, 70, 0, False)

#take the srimp
right_arm_motor.run_angle(350, 450, Stop.BRAKE, True)

#take the chest
drive_general(100, -200, 0, False)
turn_general(120)
drive_general(440, 1000, 120, True)

