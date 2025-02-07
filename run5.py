from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take shrimps and coral
drive_general(150, 200, 0, False)
turn_general(-45)
drive_general(200, 200, -45, True)
turn_general(40)
right_arm_motor.run_angle(300, -400, Stop.BRAKE, False)
drive_general(300, 400, 40, True)
wait(200)
drive_general(180, 300, 40, True)

#mission 11
left_arm_motor.run_angle(600, 350, Stop.BRAKE, True)
drive_general(40, 300, -5, True)
left_arm_motor.run_angle(600, 350, Stop.BRAKE, True)

# take shrimp and Plankton Sample
drive_general(220, -300, -5, True)
right_arm_motor.run_angle(1000, 400, Stop.BRAKE, True)
turn_general(33, False)
drive_general(40, 400, 33, True)
turn_general(73)
drive_general(10, 300, 63, True)
right_arm_motor.run_angle(600, -400, Stop.BRAKE, True)
drive_general(60, -450, 63, True)
turn_general(-80, False)
drive_general(370, -500, -80, True)
turn_general(-120)

#octupos
drive_general(250, 400, -45, True)
drive_general(500, -2000, -45, True)
