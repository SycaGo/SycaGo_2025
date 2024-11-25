from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
drive_base.settings(300, turn_acceleration=275)

drive_base.straight(150,Stop.BRAKE)

drive_base.turn(32 ,Stop.BRAKE,True)

drive_base.straight(100,Stop.BRAKE)

'''
while True:
    balls = hub.imu.heading()
    print(balls)
    '''
#drive_base.turn(20 ,Stop.BRAKE,True)

#drive_base.straight(100,Stop.BRAKE,True)

#drive_base.turn(-45,Stop.BRAKE,True)

#drive_base.straight(10,Stop.BRAKE,True)

#drive_base.turn(32,Stop.BRAKE,True)

#drive_base.straight(15,Stop.BRAKE,True)

#drive_base.straight(-15,Stop.BRAKE,True)

#drive_base.turn(16,Stop.BRAKE,True)

#drive_base.straight(36,Stop.BRAKE,True)

#drive_base.straight(-12,Stop.BRAKE,True)

#drive_base.turn(-40,Stop.BRAKE,True)

#drive_base.straight(-45,Stop.BRAKE,True)





