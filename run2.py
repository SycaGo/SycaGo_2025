from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(250, 250, 0, False)
turn_general(-90)
drive_general(100, -250, -90, True)
drive_general(600, 450, -90, True)
turn_general(-180)
left_arm_motor.run_angle(2500, -710, Stop.BRAKE,True)

#drive forward to mission 1 and take the scubadiver
drive_general(150, 300, -180, True)

left_arm_motor.run_angle(1800 , 950, Stop.BRAKE, False)
right_arm_motor.run_angle(400, -400, Stop.BRAKE,True)
right_arm_motor.run_angle(4000, -2000, Stop.BRAKE,True)


#return the arms
right_arm_motor.run_angle(2000, 2000, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, -1000, Stop.BRAKE, True)
drive_general(120, -350, -180, True)
left_arm_motor.run_angle(3000, 600, Stop.BRAKE, True)
turn_general(80, False)
drive_general(50, 350, 80, True)

#drop the shark
left_arm_motor.run_angle(10000, -800, Stop.BRAKE, True)
drive_general(35, -350, 80, True)
left_arm_motor.run_angle(10000, 900, Stop.BRAKE, True)

#backward to the wall
turn_general(40, False)
drive_general(730, -1000, 40, True)
