from parameters import left_arm_motor, right_arm_motor,hub, left_motor, right_motor, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from PID_drive import drive
from PID_Turn import turn

drive_base.settings(300)
drive_base.straight(140, Stop.BRAKE, True)
drive_base.turn(-30, Stop.BRAKE, True)
drive_base.straight(120, Stop.BRAKE, True)
drive_base.turn(-60, Stop.BRAKE, True)

#backward to the wall
drive_base.settings(250)
drive_base.straight(-70, Stop.BRAKE, True)

#drive forward to the mission
drive_base.settings(400)
drive_base.straight(620, Stop.BRAKE, True)

drive_base.turn(-90, Stop.BRAKE, True)

left_arm_motor.run_angle(3000, 860, Stop.BRAKE, True)
drive_base.straight(160, Stop.BRAKE, True)
left_arm_motor.run_angle(2000, -1200, Stop.BRAKE, True)
right_arm_motor.run_angle(4000, -2100, Stop.BRAKE, True)

#return the arms
right_arm_motor.run_angle(2000, 1600, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE, True)
drive_base.settings(300)
drive_base.straight(-130, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, -600, Stop.BRAKE, True)
drive_base.turn(75, Stop.BRAKE, True)
drive_base.straight(70, Stop.BRAKE, True)

#drop the shark
left_arm_motor.run_angle(10000, 1100, Stop.BRAKE, True)
drive_base.straight(-30, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -1100, Stop.BRAKE, True)

#backward to the wall
drive_base.turn(20, Stop.BRAKE, True)
drive_base.straight(-700, Stop.BRAKE, True)

#go back to mission 3
drive_base.settings(500)
drive_base.straight(630, Stop.BRAKE, True)
drive_base.turn(30, Stop.BRAKE, True)

right_arm_motor.run_angle(2000, -950, Stop.BRAKE, True)
'''
drive_base.settings(350)
drive_base.straight(200, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, -500, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, 300, Stop.BRAKE, True)
drive_base.straight(-20, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, 1000, Stop.BRAKE, True)
drive_base.straight(-550, Stop.BRAKE, True)
'''
