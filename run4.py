from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

# exit launch area and turn to mission
drive_general(60, 200 ,0, False)
turn_general(90)

# drive to mission 8 - tower - fast, slow, hold
drive_general(780, 500 ,90, True)
drive_general(90, 400 ,90, True)
wait(400)

# pull tower - slow, slower, release tower
drive_general(100, -200 ,90, True)
drive_general(100, -30 ,90, True)
drive_general(20, -300 ,90, True)

# drive to trident
turn_general(-52, False)
drive_general(220, 350 ,-52, True)
turn_general(40, False)

# take out the trident
left_arm_motor.run_angle(1000, 300, Stop.BRAKE, True)
drive_general(250, -1000 ,40, True)
# TAKE THE ROBOT MANUALLY FROM HERE
