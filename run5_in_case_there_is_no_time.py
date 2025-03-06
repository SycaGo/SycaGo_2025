from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

# take shrimp near the octopus
drive_general(150, 350, 0, False)
turn_general(-45)
drive_general(200, 350, -45, True)

# takes the coral and shrimp near the sonar
turn_general(-5)
drive_general(270, 400, -5, True)

# take shrimp near whale
turn_general(28)
drive_general(20, 400, 28, True)

# take plankton sample
turn_general(68)
drive_general(30, 300, 68, True)
right_arm_motor.run_angle(600, 400, Stop.BRAKE, True)
drive_general(60, -450, 68, True)

#get back to launch area
turn_general(-20)
drive_general(700, -1000, -20, True)
