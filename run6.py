from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from white_stop import white_stop

#mission 9
drive_general(100, 350, 0, False)
turn_general(-27)
drive_general(500, 400, -27, True)
turn_general(44)
drive_general(400, 200, 44, True)
wait(500)
drive_general(20, -200, 44, True)
drive_general(70, 400, 44, True)

#mission 12
drive_general(270, -300, 44, True)
turn_general(-95, False)
drive_general(150, 500, -95, True)
turn_general(-143)
drive_general(400, 500, -143, True)
drive_general(330, -500, -143, True)
turn_general(30, False)
white_stop(400)
turn_general(-5, False)
drive_general(5, -200, 0, False)
right_arm_motor.run_angle(10000, -850, Stop.BRAKE, True)
wait(500)
drive_general(100, -400, 25, True)
