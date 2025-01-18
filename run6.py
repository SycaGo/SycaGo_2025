from parameters import left_arm_motor, right_arm_motor,hub,drive_base, right_motor, left_motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(350, 450, 0, False)
turn_general(-15)
drive_general(440, 400, -15, True)

#put the shark in his place
drive_general(300, -400, -15, True)
turn_general(-100)
drive_general(150, 400, -100, True)
drive_general(40, -300, -100, True)

#back to the wall
turn_general(90)
drive_general(200, -600, 90, True)
turn_general(70)
drive_general(200, -300, 0, False)
drive_general(650, 700, 0, False)

# do the ship
right_arm_motor.run_angle(10000, 1300, Stop.BRAKE, True)
turn_general(-48)
drive_general(90, -400, -48, True)
right_arm_motor.run_angle(-10000, 1300, Stop.BRAKE, True)
turn_general(35)
drive_general(600, -1000, 35, True)
