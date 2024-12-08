from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take Krill 1
drive_general(170, 350, True)
turn_general(-42, 150, True)
drive_general(280, 350, True)
drive_general(-110, 350, True)

#take green Reef Segments
turn_general(35, 150, True)
drive_general(220, 350, True)
drive_general(-70, 350, True)

# take Krill 2
turn_general(-20, 150, True)
drive_general(200, 350, True)
turn_general(14, 150, True)
drive_general(200, 350, True)
