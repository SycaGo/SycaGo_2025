from parameters import left_arm_motor, right_arm_motor, hub, drive_base,
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

drive_general(140, 350, True)
turn_general(-25, 270, True)
drive_general(120, 350, True)
turn_general(-65, 270, True)

#backward to the wall
drive_general(-90, 250, True)

#drive forward to the mission
drive_general(640, 400, True)
turn_general(-90, 200, True)
left_arm_motor.run_angle(3000, 860, Stop.BRAKE, True)
drive_general(140, 330, True)
left_arm_motor.run_angle(1800, -1200, Stop.BRAKE, False)
right_arm_motor.run_angle(3000, -2100, Stop.BRAKE, True)

#return the arms
right_arm_motor.run_angle(2000, 1600, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE, True)
drive_general(-140, 300, True)
left_arm_motor.run_angle(3000, -600, Stop.BRAKE, True)
turn_general(70, 350, True)
drive_general(80, 300, True)

#drop the shark
left_arm_motor.run_angle(10000, 1250, Stop.BRAKE, True)
drive_general(-60, 350, True)
left_arm_motor.run_angle(10000, -1250, Stop.BRAKE, True)

#backward to the wall
turn_general(30, 300, True)
drive_general(-700, 350, False)
right_arm_motor.run_angle(2000, 300, Stop.BRAKE, True)
right_arm_motor.reset_angle()


wait(2000)

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
drive_general(-550, 400, True)
