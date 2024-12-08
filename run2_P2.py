separate
from parameters import left_arm_motor, right_arm_motor, hub, drive_base,
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

#go back to mission 3
drive_general(250, 300, True)
turn_general(90, 100, True)
drive_general(200, 300, True)
turn_general(-90, 100, True)
right_arm_motor.run_angle(2000, -1150, Stop.HOLD, True)
drive_general(350, 350, True)
turn_general(20, 250, True)
drive_general(250, 350, True)

#Click on the yellow
right_arm_motor.run_angle(2000, -1050, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, 800, Stop.BRAKE, True)
drive_general(-200, 350, True)
turn_general(-15, 350, True)

#go back home
drive_general(-550, 400, True)
