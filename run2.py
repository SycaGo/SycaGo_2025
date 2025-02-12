from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(400, 350, 0, False)
right_arm_motor.run_angle(100, -150, Stop.BRAKE,True)
right_arm_motor.run_angle(100, 70, Stop.BRAKE,True)
drive_general(100, -400, 0, False)
turn_general(60)
drive_general(350, 400, 0, False)
turn_general(-56)
drive_general(200, 400, 0, False)
turn_general(-55)
drive_general(140, 400, 0, False)
right_arm_motor.run_angle(600, 200, Stop.BRAKE,True)


'''
drive_general(90, 100, 0, False)
right_arm_motor.run_angle(70, -60, Stop.BRAKE,True)
drive_general(70, 100, 0, False)
'''
