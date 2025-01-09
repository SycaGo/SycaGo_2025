from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
drive_general(600, 550, 0, False)
turn_general(25)
drive_general(330, 450, 25, True)
wait(400)
right_arm_motor.run_angle(300, 400, Stop.BRAKE, True)
turn_general(120)
left_arm_motor.run_angle(800, 240, Stop.BRAKE, True)
drive_general(100, -400, 120, True)
left_arm_motor.run_angle(800, -220, Stop.BRAKE, True)
drive_general(50, 200, 120, True)
turn_general(60)
drive_general(250, 500, 60, True)
turn_general(-25)
drive_general(620, 800, -25, True)
