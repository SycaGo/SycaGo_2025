from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(310, 400)
turn_general(30)
drive_general(160, 350)
turn_general(60)

#drive forward to the mission
drive_general(110, 150)
drive_general(100, 70)
right_arm_motor.run_angle(200, 300, Stop.BRAKE, True)
drive_general(140, -200)

#put the srimp in the house
turn_general(100)
drive_general(40, 300)

right_arm_motor.run_angle(10000, -300, Stop.BRAKE, True)
turn_general(-15)

#Alignment on a wall
drive_general(450, -350)
left_arm_motor.run_angle(5000, 900, Stop.BRAKE, True)
left_arm_motor.run_angle(5000, -200, Stop.BRAKE, True)
drive_general(800, 900)
