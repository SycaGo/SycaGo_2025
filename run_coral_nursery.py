from parameters import left_arm_motor, right_arm_motor,hub
from pybricks.parameters import Stop
from pybricks.tools import wait
from pid_drive import drive
from pid_turn import turn

drive(2, 0.003, 1, 0, 350, 15)
turn(90, 7, 0.001, 0)
drive(3, 0.003, 1, 0, 350, 5)
turn(-90, 7, 0.001, 0)
drive(2, 0.003, 1, 0, 350, 30)
turn(-90, 7, 0.003, 0)
left_arm_motor.run_angle(3000, 750, Stop.BRAKE, True)


#right_arm_motor.run_angle(5000, -1200 , Stop.BRAKE, True)
#right_arm_motor.run_angle(6000, 1200 , Stop.BRAKE, True)

