from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_alignment import line_alignment

#mission 9
drive_general(150, 250, 0, False)
drive_general(80, 100, 0, False)
drive_general(90, -400, 0, False)
turn_general(-33)
drive_general(490, 550, -33, True)
turn_general(78)
drive_general(350, 300, 78, True)
wait(800)
drive_general(20, -200, 78, True)
drive_general(100, 400, 78, True)
drive_general(20, -200, 78, True)
drive_general(100, 400, 78, True)

#mission 12
drive_general(270, -350, 78, True)
turn_general(-92)
drive_general(150, 500, -92, True)
turn_general(-25)
line_alignment(250)
turn_general(-15)
drive_general(10, -300, -15, True)
right_arm_motor.run_angle(10000, -720, Stop.BRAKE, True)
wait(500)
turn_general(-60)
drive_general(50, 400, -60, True)
turn_general(10)
drive_general(50, 400, 10, True)
drive_general(95, -400, 10, True)
