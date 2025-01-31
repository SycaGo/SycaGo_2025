from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(250, 250, 0, False)
turn_general(-90)
drive_general(100, -250, 0, False)
drive_general(600, 450, 0, False)
turn_general(-90)
left_arm_motor.run_angle(2500, -700, Stop.BRAKE,True)

#drive forward to mission 1 and take the scubadiver
drive_general(140, 300, -90, True)

left_arm_motor.run_angle(1800, 900, Stop.BRAKE, False)
right_arm_motor.run_angle(400, -400, Stop.BRAKE,True)
right_arm_motor.run_angle(4000, -1600, Stop.BRAKE,True)

#return the arms
right_arm_motor.run_angle(2000, 1500, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, -1000, Stop.BRAKE, True)
drive_general(100, -350, -90, True)
left_arm_motor.run_angle(3000, 600, Stop.BRAKE, True)
turn_general(80)
drive_general(50, 300, 80, True)

#drop the shark
left_arm_motor.run_angle(10000, -800, Stop.BRAKE, True)
drive_general(35, -350, 80, True)
left_arm_motor.run_angle(10000, -300, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, 900, Stop.BRAKE, True)

#backward to the wall
turn_general(40)
drive_general(730, -1000, 40, True)
