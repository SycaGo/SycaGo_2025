from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take Krill 1
drive_general(170, 350, True)
turn_general(-50, 275, True)
drive_general(320, 350, True)
drive_general(-90, 350, True)

#take green Reef Segments
turn_general(45 ,275, True)
drive_general(160, 350, True)

# take Krill 2
turn_general(-15, 275, True)
drive_general(200, 350, True)
turn_general(15, 275, True)
drive_general(250, 350, True)
drive_general(-50, 350, True)
turn_general(30, 275, True)
drive_general(-200, 350, True)
