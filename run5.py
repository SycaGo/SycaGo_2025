from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take shrimps and coral
<<<<<<< HEAD
drive_general(150, 350, 0, False)
turn_general(-45)
drive_general(200, 350, -45, True)
turn_general(-5)
right_arm_motor.run_angle(300, -400, Stop.BRAKE, False)
drive_general(300, 400, -5, True)
wait(200)
drive_general(180, 300, -5, True)

#mission 11
left_arm_motor.run_angle(600, -350, Stop.BRAKE, True)
drive_general(40, 300, -5, True)
left_arm_motor.run_angle(600, -350, Stop.BRAKE, True)

# take shrimp and Plankton Sample
drive_general(280, -300, -5, True)
right_arm_motor.run_angle(1000, 400, Stop.BRAKE, True)
turn_general(33, False)
drive_general(60, 400, 33, True)
turn_general(63)
drive_general(10, 300, 63, True)
right_arm_motor.run_angle(600, -400, Stop.BRAKE, True)
drive_general(30, -450, 63, True)
turn_general(-80, False)
drive_general(330, -500, -80, True)
turn_general(-120)

#octupos
drive_general(250, 500, -120, True)
drive_general(500, -1000, -120, True)
=======
drive_general(150, 250, 0, False)
turn_general(-45)
drive_general(180, 250, -45, True)
turn_general(39.5)
right_arm_motor.run_angle(1000, 400, Stop.BRAKE, False)
left_arm_motor.run_angle(2000, 400, Stop.BRAKE, False)
drive_general(400, 400, 39.5, True)
wait(200)
drive_general(120, 100, 39.5, True)

#mission 11
left_arm_motor.run_angle(600, -700, Stop.BRAKE, True)

# take shrimp and Plankton Sample
drive_general(250, -300, 0, False)
right_arm_motor.run_angle(1000, 400, Stop.BRAKE, True)
turn_general(33)
drive_general(30, 400, 33, True)
turn_general(33)
drive_general(10, 300, 33, True)
right_arm_motor.run_angle(600, -400, Stop.BRAKE, True)
drive_general(30, -400, 33, True)
turn_general(-80)
drive_general(300, -400, -80, True)
turn_general(-40)

#octupos
drive_general(250, 300, -40, True)
drive_general(500, -2000, -40, True)
>>>>>>> parent of fbe0b52 (Update run5.py)
