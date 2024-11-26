from parameters import left_arm_motor, right_arm_motor,hub, left_motor, right_motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from PID_drive import drive
from PID_Turn import turn

drive(2, 0, 0, 0, 350, 13)
turn(-30, 8, 0, 2)
drive(1.5, 0, 0, 0, 350, 6)
turn(-60, 9, 0.003, 2)

#backward to the wall
drive(1.5, 0, 0, 0, -250, 5)

#drive forward to the mission
drive(1.5, 0, 0, 0, 400, 62)
turn(-90, 6, 0.006, 2.5)
left_arm_motor.run_angle(3000, 860, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, 240, 17)
left_arm_motor.run_angle(2000, -1200, Stop.BRAKE, True)
right_arm_motor.run_angle(3500, -2300, Stop.BRAKE, True)

#return the arms
right_arm_motor.run_angle(2000, 1700, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, -300, 13)
left_arm_motor.run_angle(3000, -600, Stop.BRAKE, True)
turn(75, 7, 0.007, 2)
drive(1.5, 0, 0, 0, 400, 5)

#drop the shark
left_arm_motor.run_angle(10000, 1100, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, -350, 3)
left_arm_motor.run_angle(10000, -1100, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, -350, 4)
turn(27, 7, 0.007, 2)

#mission 3
right_arm_motor.run_angle(2000, -1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, 350, 10)
right_arm_motor.run_angle(2000, -1000, Stop.BRAKE, True)
right_arm_motor.run_angle(2000, 1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, 350, -10)
right_arm_motor.run_angle(2000, 900, Stop.BRAKE, True)





'''
#backward to the wall
turn(20, 7, 0.007, 2)
drive(1.5, 0, 0, 0, -500, 70)

#go back to mission 3
drive(1.5, 0, 0, 0, 500, 55)
turn(20, 7, 0.007, 2)
right_arm_motor.run_angle(2000, -1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, 350, 10)
right_arm_motor.run_angle(2000, -300, Stop.BRAKE, True)



#for ohad
#drive(1.5, 0, 0, 0, 120, 8)
#left_arm_motor.run_angle(2000, 120, Stop.BRAKE, True)
#drive(1.5, 0, 0, 0, 250, 15)
#drive(1.5, 0, 0, 0, -250, 15)

#to check the motors
#left_motor.run_angle(200, 1000, Stop.BRAKE, False)
#right_motor.run_angle(200, 1000, Stop.BRAKE, True)

#right_motor.run_angle(200, 1000, Stop.BRAKE, True)
'''
