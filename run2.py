from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

#put the coral on the yellow
drive_general(250, 350, 0, False)
left_arm_motor.run_angle(300, -80, Stop.BRAKE,True)
drive_general(10, -100, 0, False)
wait(50)
left_arm_motor.run_angle(1000, -100, Stop.BRAKE,True)
drive_general(180, 350, 0, False)
turn_general(-10)
left_arm_motor.run_angle(50, 80, Stop.BRAKE,True)
drive_general(100, -200, -10, True)

#free shark
turn_general(60)
drive_general(300, 350, 60, True)
turn_general(-10)
drive_general(200, 350, -10, True)
turn_general(-45)
drive_general(10, 200, -45, True)
left_arm_motor.run_angle(10000, 400, Stop.BRAKE,True)

