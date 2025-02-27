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
right_arm_motor.run_angle(200, 500, Stop.BRAKE, False)

# arrive to the sonar
drive_general(300, 400, -5, True)
wait(200)
drive_general(180, 300, -5, True)

# turn sonar model
left_arm_motor.run_angle(600, 350, Stop.BRAKE, True)
drive_general(40, 300, -5, True)
left_arm_motor.run_angle(600, 500, Stop.BRAKE, True)

# take shrimp near whale
drive_general(220, -300, -5, True)
right_arm_motor.run_angle(1000, -500, Stop.BRAKE, True)
turn_general(28)

# take plankton sample
drive_general(40, 400, 28, True)
turn_general(68)
drive_general(10, 300, 68, True)
right_arm_motor.run_angle(600, 400, Stop.BRAKE, True)

# arrive to the octupos
drive_general(60, -450, 68, True)
turn_general(-12)
drive_general(370, -500, -12, True)
turn_general(-52)

#octupos
drive_general(250, 300, -52, True)

#go home
drive_general(500, -1000, -52, True)
