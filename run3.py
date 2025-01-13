from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(300, 500, 0, False)
turn_general(30)
drive_general(170, 330 , 30, True)
turn_general(60)

#drive forward to the mission
drive_general(105, 150, 60, True)
drive_general(110, 60, 60, True)
right_arm_motor.run_angle(100, 120, Stop.BRAKE, True)
right_arm_motor.run_angle(500, 200, Stop.BRAKE, True)
drive_general(110, -200, 60, True)

#put the srimp in the house
turn_general(100)
drive_general(60, 300, 100, True)

right_arm_motor.run_angle(10000, -300, Stop.BRAKE, True)
turn_general(-20)

#Alignment on a wall
drive_general(420, -700, -20, True)
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -250, Stop.BRAKE, True)
drive_general(500, 1000,0, False)
turn_general(60)
drive_general(350, 1000, 60, True)
