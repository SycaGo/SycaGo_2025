from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait

def drive_general(distance, speed, bool):
    
    drive_base.settings(straight_speed=speed)
    drive_base.straight(distance, Stop.BRAKE, bool)

