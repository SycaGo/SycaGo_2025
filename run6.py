from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general


#take Krill 1
drive_general(160, 350)
turn_general(-45, 200, True)
drive_general(240, 350)
drive_general(70, -350)

# take Krill 2
turn_general(35, 200, True)
drive_general(180, 350)

#take green Reef Segments
turn_general(-20, 200, True)
drive_general(150, 350)

# do the Sonar Discovery

# take or not Krill 3

# take Plankton Sample
