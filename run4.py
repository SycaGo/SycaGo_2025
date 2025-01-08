from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
drive_general(220, 400, 0, False)
turn_general(30)
drive_general(350, 400, 30, True)
turn_general(-30)
drive_general(450,400, -30, False)
left_arm_motor.run_angle(400,270,Stop.BRAKE, True)
drive_general(60,-30, -30, True)
left_arm_motor.run_angle(510,100,Stop.BRAKE, True)
drive_general(150,-30, -30, True)
left_arm_motor.run_angle(500,-70,Stop.BRAKE, True)
drive_general(50,400, -30, True)
left_arm_motor.run_angle(500,70,Stop.BRAKE, True)
turn_general(50)
drive_general(700,-700, 50, True)
turn_general(50)
drive_general(50,700, 50, True)

