from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait

def turn_general(turn_degrees, speed, dsync):
    drive_base.settings(turn_rate=speed)
    drive_base.turn(turn_degrees, Stop.BRAKE, dsync)
