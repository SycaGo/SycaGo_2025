from parameters import left_arm_motor, right_arm_motor, hub, drive_base,
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(-20, 300, True)
drive_general(350, 300, True)
turn_general(30, 250, True)
drive_general(180, 350, True)
turn_general(60, 130, True)
drive_general(200, 300, True)

#drive forward to the mission
drive_general(110, 50, True)
drive_general(-300, 100, True)

#get the treasure ches in the oneway
drive_general(200, 500, True)


