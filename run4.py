from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general
drive_general(400, 400)
turn_general(40)
drive_general(230, 450)
turn_general(-38)
drive_general(300, 450)
right_arm_motor.run_angle(300, 280, Stop.BRAKE, True)
drive_general(200, -100)
