from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(290, 500, 0, False)
turn_general(30)
drive_general(170, 200, 30, True)
turn_general(60)

#drive forward to the mission
drive_general(100, 300, 0, False)
drive_general(110, 60, 0, False)
right_arm_motor.run_angle(100, 120, Stop.BRAKE, True)
right_arm_motor.run_angle(500, 200, Stop.BRAKE, True)
drive_general(110, -200, 0, False)

#put the srimp in the house
turn_general(100)
drive_general(60, 300, 100, True)

right_arm_motor.run_angle(8000, -300, Stop.BRAKE, True)
turn_general(-20)

#Alignment on a wall
drive_general(420, -600, -20, True)
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(5000, -250, Stop.BRAKE, True)
drive_general(500, 550,-20, True)
turn_general(50)
drive_general(350, 600, 50, True)
