from parameters import left_arm_motor, right_arm_motor,hub
from pybricks.parameters import Stop
from pybricks.tools import wait
from pid_drive import drive
from pid_turn import turn

drive(2, 0.003, 1, 0, 350, 17)
turn(-90, 7, 0.009, 0)
drive(3, 0.003, 1, 0, -350, 3)
drive(1, 0, 1, 0, 350, 53)
turn(-90, 7, 0, 0)
left_arm_motor.run_angle(3000, 790, Stop.BRAKE, True)
drive(1.5, 0.003, 1, 0, 350, 13)
left_arm_motor.run_angle(3000, -900, Stop.BRAKE, True)
right_arm_motor.run_angle(6500, -1700, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, -250, Stop.BRAKE, True)
right_arm_motor.run_angle(6000, 1600, Stop.BRAKE, True)
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, -350, 13)
left_arm_motor.run_angle(3000, -600, Stop.BRAKE, True)
turn(70, 7, 0, 0)
drive(1.5, 0, 0, 0, 350, 7)
left_arm_motor.run_angle(9000, 1000, Stop.BRAKE, True)
turn(40, 7, 0, 0)
drive(1.5, 0, 0, 0, -350, 2)
left_arm_motor.run_angle(6000, -1000, Stop.BRAKE, True)
drive(1.5, 0, 0, 0, -350, 60)









