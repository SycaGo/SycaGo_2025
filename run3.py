from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(120, 350, 0, False)
turn_general(90)
drive_general(650, -500, 90, True)
turn_general(15)
drive_general(150, -600, 15, True)
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -350, Stop.BRAKE, True)
drive_general(300, 550, 0, False)
turn_general(-90)
drive_general(70, 150, -90, True)
drive_general(120, 70, -90, True)
right_arm_motor.run_angle(100, 120, Stop.BRAKE, True)
right_arm_motor.run_angle(500, 200, Stop.BRAKE, True)
drive_general(100, -200, -90, True)
turn_general(100)
drive_general(130, 300, 100, True)
right_arm_motor.run_angle(500, -200, Stop.BRAKE, True)
turn_general(-120)
