from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take Krill 1
drive_general(170, 350, True)
turn_general(-30, 275, True)
drive_general(160, 350, True)

#take green Reef Segments
turn_general(36 ,275, True)
drive_general(160, 350, True)

# take Krill 2
#reaset gyro
hub.imu.reset_heading(0)
turn_general(-30, 275, True)
drive_general(200, 350, True)
drive_general(-120, 350, True)

# take Krill 3
#reaset gyro
hub.imu.reset_heading(0)
turn_general(44, 275, True)
drive_general(200, 350, True)
drive_general(-130, 350, True)

# turn to wall
turn_general(-34, 275, True)

# forward the wall
drive_general(330, 350, True)

#reaset gyro
hub.imu.reset_heading(0)

#take Plankton Sample
drive_general(-170, 350, True)
turn_general(82, 150, True)
drive_general(90, 300, True)
drive_general(-170, 350, True)

#take Unknown Creature
turn_general(-80, 250, True)
drive_general(-450, 350, True)
turn_general(-28, 275, True)
drive_general(180, 350, True)
drive_general(-130, 350, True)
turn_general(-30, 275, True)
drive_general(-300 , 350, True)
