from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

# taking 2 corals and shrimp and water sample near the rd lanunch area
drive_general(640, 500, 0, False)
turn_general(24)

# closing the cage and driving to the next sample
right_arm_motor.run_angle(300, 330, Stop.BRAKE, False)
drive_general(280, 450, 24, True)

# turning to take the sample
turn_general(144)
drive_general(40, 200, 144, True) 

# take the sample
left_arm_motor.run_angle(600, 280, Stop.BRAKE, True)
drive_general(100, -400, 144, True)
left_arm_motor.run_angle(300, -250, Stop.BRAKE, True)

# driving back to launch area
drive_general(50, 200, 144, True)
turn_general(211)
drive_general(250, 1000, 211, True)
turn_general(176)
drive_general(660, 1000, 176, True)
