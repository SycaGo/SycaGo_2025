from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(140, 300, 0, False)
turn_general(-25)
drive_general(120, 300, -25, True)
turn_general(-65)

#backward to the wall
drive_general(80, -200, -65, True)

drive_general(600, 450, 0, False)
turn_general(-90)
left_arm_motor.run_angle(3000, 860, Stop.BRAKE,True)

#drive forward to mission 1 and take the scubadiver
drive_general(140, 350, -90, True)

left_arm_motor.run_angle(1800, -1200, Stop.BRAKE, False)
right_arm_motor.run_angle(3000, -2100, Stop.BRAKE,True)

#return the arms
right_arm_motor.run_angle(2000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE, True)
drive_general(140, -350, -90, True)
left_arm_motor.run_angle(3000, -600, Stop.BRAKE, True)
turn_general(70)
drive_general(50, 300, 70, True)
#drop the shark
left_arm_motor.run_angle(10000, 1250, Stop.BRAKE, True)
drive_general(60, -350, 70, True)
left_arm_motor.run_angle(10000, -1250, Stop.BRAKE, True)

#backward to the wall
turn_general(37)
drive_general(700, -500, 37, True)

#reset right arm motor
right_arm_motor.run_angle(2000, 250, Stop.BRAKE, True)
