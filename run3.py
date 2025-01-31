from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

#drive straight to mission 6
drive_general(120, 350, 0, False)
turn_general(-90)
wait(100)
drive_general(370, 350, -90, True)
turn_general(90)
wait(100)

#get up the toren
drive_general(150, 110, 90, True)
drive_general(80, 50, 90, True)

#take the srimp
right_arm_motor.run_angle(350, 400, Stop.BRAKE, True)

#take the chest
drive_general(180, -350, 90, True)

#go backward to mission 3
turn_general(93)
drive_general(400, -350, 93, True)
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -365, Stop.BRAKE, True)
drive_general(500, 1000, 93, True)
turn_general(50)
drive_general(300, 1000, 50 , True)
