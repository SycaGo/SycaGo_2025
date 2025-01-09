from parameters import left_arm_motor, right_arm_motor,hub,drive_base, right_motor, left_motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(200,400, 0, False)
turn_general(-90)
drive_general(530, 400, -90, True)
turn_general(-95)
drive_general(200, 200, -95, True)
drive_general(10, -300, -95, True)
drive_general(30, 400, -95, True)
drive_general(100, -100, -95, True)
turn_general(90)
drive_general(200, -600, 90, True)
turn_general(90)
drive_general(390, -440, 90, True)
drive_general(620, 450, 90, True)
turn_general(-45)
right_arm_motor.run_angle(10000, 1300, Stop.BRAKE, True)
drive_general(90, -400, -45, True)
right_arm_motor.run_angle(-10000, 1000, Stop.BRAKE, True)
turn_general(45)
drive_general(700, -800, 45, True)

