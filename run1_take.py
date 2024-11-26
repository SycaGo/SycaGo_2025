from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
drive_base.settings(300, turn_acceleration=275)

drive_base.straight(150,Stop.BRAKE)

drive_base.turn(32 ,Stop.BRAKE,True)

drive_base.straight(230,Stop.BRAKE)

'''
while True:
    angle = hub.imu.heading()
    print(angle)
    '''
drive_base.turn(-50 ,Stop.BRAKE,True)

drive_base.straight(150,Stop.BRAKE,True)

drive_base.turn(25,Stop.BRAKE,True)

drive_base.straight(170,Stop.BRAKE,True)

drive_base.straight(-270,Stop.BRAKE,True)

drive_base.turn(25,Stop.BRAKE,True)

drive_base.straight(370,Stop.BRAKE,True)

drive_base.straight(-800,Stop.BRAKE,True)
