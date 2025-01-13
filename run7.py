from parameters import left_arm_motor, right_arm_motor,hub,drive_base, right_motor, left_motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(200,500, 0, False)
turn_general(-90)
drive_general(495, 500, -90, True)
turn_general(-90)
drive_general(170, 300, -90, True)
drive_general(10, -300, -90, True)
drive_general(20, 400, -90, True)
drive_general(100, -300, -90, True)
turn_general(90)
drive_general(200, -600, 90, True)
turn_general(90)
drive_general(320, -440, 90, True)
drive_general(640, 500, 0, False)
turn_general(-50)
right_arm_motor.run_angle(10000, 1300, Stop.BRAKE, True)
drive_general(110, -400, -50, True)
right_arm_motor.run_angle(-10000, 1300, Stop.BRAKE, True)
turn_general(45)
drive_general(200, -1000, 45, True)
turn_general(-45)
drive_general(550, -1000, -45, True)
