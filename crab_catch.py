from parameters import left_arm_motor, right_arm_motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from parameters import hub
from parameters import drive_base
from drive import drive
from turn import turn

drive(1, 0, 0, 0, 300, 85)
drive(0.5, 0, 0, 0, -50, 20)
drive_base.turn(5, Stop.BRAKE, True)
drive_base.settings(straight_speed=400)
drive_base.straight(-640, Stop.BRAKE, True)
