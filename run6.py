from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

drive_general(10, 450, True)

#take Krill 1
drive_general(170, 450, True)
turn_general(-42, 150, True)
drive_general(300, 450, True)
drive_general(-110, 450, True)

#take green Reef Segments
turn_general(35, 150, True)
drive_general(220, 450, True)
drive_general(-140, 450, True)

# take Krill 2
turn_general(-23, 150, True)
drive_general(200, 450, True)

# do the Sonar Discovery
turn_general(20, 150, True)
drive_general(300, 450, True)
turn_general(40, 150, True)
drive_general(-200, 450, True)

# take or not Krill 3
hub.imu.reset_heading(0)
turn_general(35, 150, True)
drive_general(220, 600, True)
drive_general(-200, 450, True)

# take Plankton Sample
turn_general(20, 150, True)
drive_general(220, 200, True)
drive_general(-220, 450, True)
drive_general(150, 450, True)
