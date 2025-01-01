from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(310, 400)
turn_general(30)
drive_general(170, 350)
turn_general(60)

#drive forward to the mission
drive_general(140, 250)
drive_general(110, 70)
drive_general(90, -300)
turn_general(-110)
right_arm_motor.run_angle(1000, -122, Stop.BRAKE, True)
drive_general(100, 350)
turn_general(-28)
right_arm_motor.run_angle(1000, -30, Stop.BRAKE, True)
drive_general(50, 350)

#take the scubadiver
right_arm_motor.run_angle(100, 150, Stop.BRAKE, True)

turn_general(20)
drive_general(150, -350)
turn_general(50)
drive_general(60, 350)
turn_general(15)
drive_general(70, 350)
right_arm_motor.run_angle(100, -120, Stop.BRAKE, True)

#put the scubadiver on the yellow line
drive_general(30, 350)

#go back home
drive_general(700, -600)
