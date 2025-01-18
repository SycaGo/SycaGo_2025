from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(640, 400, 0, False)
turn_general(22)
drive_general(315, 450, 22, True)
wait(400)
right_arm_motor.run_angle(300, 350, Stop.BRAKE, True)
turn_general(120)
drive_general(40, 200, 120, True)
left_arm_motor.run_angle(600, 250, Stop.BRAKE, True)
drive_general(100, -400, 120, True)
left_arm_motor.run_angle(300, -250, Stop.BRAKE, True)
drive_general(50, 200, 0, False)
turn_general(62)
drive_general(250, 500, 62, True)
turn_general(-25)
drive_general(630, 1000, -25, True)
