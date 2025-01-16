from parameters import left_arm_motor, right_arm_motor,hub,drive_base, right_motor, left_motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#put the shark in place
drive_general(400, 500, 0, False)
turn_general(-12)
drive_general(200, 400, -12, True)
drive_general(140, 100, -12, True)

drive_general(100, -400, -12, True)
drive_general(100, -100, -12, True)
turn_general(-110)
drive_general(70, 150, -119, True)
turn_general(10)
drive_general(50, 600, 10, True)
wait(500)
drive_general(30, -300, 10, True)
drive_general(60, 600, 10, True)
wait(500)
drive_general(40, -300, 10, True)


#back to the wall
turn_general(90)
drive_general(250, -600, 90, True)
turn_general(80)
drive_general(200, -600, 0, False)
drive_general(650, 700, 0, True)

# do the ship
right_arm_motor.run_angle(10000, 1300, Stop.BRAKE, True)
turn_general(-40)
drive_general(90, -400, -50, True)
right_arm_motor.run_angle(-10000, 1300, Stop.BRAKE, True)
turn_general(35)
drive_general(600, -1000, 35, True)
