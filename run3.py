from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(110, 300, 0, False)
turn_general(91)
drive_general(700, -500, 91, True)
turn_general(15)
drive_general(110, -600, 15, True)
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -365, Stop.BRAKE, True)
drive_general(300, 550, 0, False)
turn_general(-90)
drive_general(70, 150, -90, True)
drive_general(130, 70, -90, True)
right_arm_motor.run_angle(100, 120, Stop.BRAKE, True)
right_arm_motor.run_angle(500, 200, Stop.BRAKE, True)
drive_general(100, -200, -90, True)
turn_general(120)
drive_general(440, 700, 120, True)
