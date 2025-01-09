from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take shrimps and coral
drive_general(150, 400, 0, False)
turn_general(-37)
drive_general(180, 400, -37, True)
turn_general(30)
left_arm_motor.run_angle(300, 400, Stop.BRAKE, False)
drive_general(470, 400, 32, True)
drive_general(200, 400, 32, True)

#mission 13
drive_general(10, -200, 25, True)
turn_general(25)
drive_general(200, -200, 25, True)

# take shrimp and Plankton Sample
turn_general(37)
left_arm_motor.run_angle(300, -400, Stop.BRAKE, True)
drive_general(120, 300, 37, True)
turn_general(25)
left_arm_motor.run_angle(300, 400, Stop.BRAKE, True)
drive_general(20, -400, 25, True)

#octupos
turn_general(-90)
drive_general(400, -400, -90, True)
turn_general(-40)
drive_general(200, 400, -40, True)
drive_general(450, -400, -40, True)
