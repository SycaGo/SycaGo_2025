from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_aligment import line_alignment

#mission 9
drive_general(210, 100)
drive_general(60, -400)
turn_general(-33)
drive_general(500, 400)
turn_general(75)
drive_general(350, 180)
wait(800)
drive_general(20, -200)
drive_general(100, 200)
drive_general(20, -200)
drive_general(100, 200)

#mission 12
drive_general(290, -400)
turn_general(-92)
drive_general(150, 400)
turn_general(-25)
line_alignment(200)
turn_general(-15)
drive_general(10, -300)
right_arm_motor.run_angle(10000, -720, Stop.BRAKE, True)
wait(1000)
turn_general(-60)
drive_general(50, 400)
turn_general(28)
drive_general(50, 400)
drive_general(80, -400)
