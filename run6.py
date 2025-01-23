from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from line_alignment import line_alignment

#mission 9
drive_general(150, 150, 0, False)
drive_general(30, 100, 0, False)
drive_general(80, -400, 0, False)
turn_general(-27)
drive_general(510, 400, -27, True)
turn_general(70)
drive_general(400, 200, 70, True)
wait(500)
drive_general(20, -200, 70, True)
drive_general(70, 400, 70, True)
wait(300)
drive_general(20, -200, 70, True)
drive_general(70, 400, 70, True)

#mission 12
drive_general(270, -300, 70, True)
turn_general(-95)
drive_general(150, 500, -95, True)
turn_general(-48)
drive_general(400, 300, -48, True)
drive_general(370, -300, -48, True)
turn_general(20)
line_alignment(250)
turn_general(-10)
right_arm_motor.run_angle(10000, -720, Stop.BRAKE, True)
wait(500)
drive_general(100, -400, 25, True)

