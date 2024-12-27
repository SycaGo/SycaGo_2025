from parameters import left_arm_motor, right_arm_motor, hub, drive_base,
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(350, 300)
turn_general(30)
drive_general(180, 350)
turn_general(60)
drive_general(200, 300)

#drive forward to the mission
drive_general(110, 70)
drive_general(300, -100)

#get the treasure ches in the oneway
drive_general(200, 500)
