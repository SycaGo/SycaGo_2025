from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_alignment import line_alignment

#mission 9
drive_general(150, 150, 0, False)
drive_general(80, 100, 0, False)
drive_general(90, -400, 0, False)
turn_general(-27)
drive_general(490, 550, -27, True)
turn_general(72)
drive_general(350, 300, 72, True)
wait(800)
drive_general(20, -200, 72, True)
drive_general(50, 400, 72, True)
drive_general(20, -200, 72, True)
drive_general(50, 400, 72, True)

#mission 12
drive_general(270, -300, 72, True)
turn_general(-92)
drive_general(150, 500, -92, True)
turn_general(-25)
drive_general(100, 300, -25, True)
line_alignment(250)
turn_general(-10)
drive_general(10, -300, -10, True)
right_arm_motor.run_angle(10000, -720, Stop.BRAKE, True)
wait(500)
turn_general(-50)
drive_general(70, 300, -50, True)
turn_general(10)
drive_general(50, 400, 10, True)
drive_general(95, -400, 10, True)
