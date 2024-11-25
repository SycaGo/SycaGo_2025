from parameters import left_arm_motor, right_arm_motor, hub, drive_base,
from pybricks.parameters import Stop
from pybricks.tools import wait

drive_base.settings(300)
drive_base.straight(140, Stop.BRAKE, True)
drive_base.turn(-30, Stop.BRAKE, True)
drive_base.straight(120, Stop.BRAKE, True)
drive_base.turn(-60, Stop.BRAKE, True)

#backward to the wall
drive_base.settings(250)
drive_base.straight(-90, Stop.BRAKE, True)

#drive forward to the mission
drive_base.settings(400)
drive_base.straight(640, Stop.BRAKE, True)
drive_base.turn(-90, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 860, Stop.BRAKE, True)
drive_base.straight(140, Stop.BRAKE, True)
left_arm_motor.run_angle(2000, -1200, Stop.BRAKE, False)
right_arm_motor.run_angle(3500, -2000, Stop.BRAKE, True)

#return the arms
right_arm_motor.run_angle(2000, 1600, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE, True)
drive_base.settings(300)
drive_base.straight(-140, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, -600, Stop.BRAKE, True)
drive_base.turn(75, Stop.BRAKE, True)
drive_base.straight(40, Stop.BRAKE, True)

#drop the shark
left_arm_motor.run_angle(10000, 1250, Stop.BRAKE, True)
drive_base.straight(-60, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -1250, Stop.BRAKE, True)

#backward to the wall
drive_base.turn(37, Stop.BRAKE, True)
drive_base.straight(-700, Stop.BRAKE, True)
wait(3000)

#go back to mission 3
drive_base.straight(250, Stop.BRAKE, True)
drive_base.turn(90, Stop.BRAKE, True)
drive_base.straight(230, Stop.BRAKE, True)
drive_base.turn(-90, Stop.BRAKE, False)
right_arm_motor.run_angle(2000, -1150, Stop.BRAKE, True)
drive_base.straight(350, Stop.BRAKE, True)
drive_base.turn(15, Stop.BRAKE, True)
drive_base.straight(120, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, -600, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, 750, Stop.BRAKE, True)
drive_base.straight(-200, Stop.BRAKE, True)
drive_base.turn(20, Stop.BRAKE, False)
drive_base.straight(-650, Stop.BRAKE, True)




'''
right_arm_motor.run_angle(2000, -1200, Stop.BRAKE, True)
drive_base.settings(350)
drive_base.straight(200, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, -500, Stop.BRAKE, True)


right_arm_motor.run_angle(2000, 300, Stop.BRAKE, True)
drive_base.straight(-20, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, 1000, Stop.BRAKE, True)
drive_base.straight(-550, Stop.BRAKE, True)

drive_base.settings(500)

drive_base.straight(700, Stop.BRAKE, True)
drive_base.settings(300)
drive_base.straight(200, Stop.BRAKE, True)

drive_base.settings(450)
drive_base.straight(550, Stop.BRAKE, True)
wait(200)
drive_base.straight(-200, Stop.BRAKE, True)

'''
