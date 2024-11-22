from parameters import left_arm_motor, right_arm_motor,hub, left_motor, right_motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from PID_drive import drive
from PID_Turn import turn

drive(2, 0.003, 1, 0, 300, 10)
turn(-30, 8, 0.003, 2)
drive(2, 0.003, 1, 0, 300, 6)
turn(-60, 9, 0.003, 2)

#backward to the wall
drive(3, 0.003, 1, 0, -250, 5)

#drive forward to the mission
drive(0, 0, 0, 0, 400, 51)
turn(-92, 9, 0.006, 2.5)
left_arm_motor.run_angle(3000, 860, Stop.BRAKE, True)
drive(1.5, 0, 1, 0, 240, 16)
left_arm_motor.run_angle(2000, -1200, Stop.BRAKE, True)
right_arm_motor.run_angle(4000, -2100, Stop.BRAKE, True)

#return the arms
right_arm_motor.run_angle(2000, 1700, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, -300, 13)
left_arm_motor.run_angle(3000, -600, Stop.BRAKE, True)
turn(75, 7, 0.007, 2)
drive(1.5, 0, 0, 0, 400, 7)

#drop the shark
left_arm_motor.run_angle(10000, 1100, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, -350, 3)
left_arm_motor.run_angle(10000, -1100, Stop.BRAKE, True)

#backward to the wall
turn(20, 7, 0.007, 2)
drive(1.5, 0, 0, 0, -500, 70)

#go back to mission 3
drive(1.5, 0, 0, 0, 500, 55)
turn(20, 7, 0.007, 2)
right_arm_motor.run_angle(2000, -1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, 350, 10)
right_arm_motor.run_angle(2000, -300, Stop.BRAKE, True)
