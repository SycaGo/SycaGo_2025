from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

<<<<<<< HEAD
#drive straight to mission 6
drive_general(120, 350, 0, False)
turn_general(-90)
wait(100)
drive_general(370, 350, -90, True)
turn_general(90, False, Kp= 6)
wait(100)

#get up the toren
drive_general(180, 110, 90, True)
drive_general(80, 50, 90, True)

#take the srimp
right_arm_motor.run_angle(350, 400, Stop.BRAKE, True)

#take the chest
drive_general(180, -350, 90, True)
=======
drive_general(125, 300, 0, False)
turn_general(93)
>>>>>>> parent of c71121c (Update run3.py)

# released the shrimp
turn_general(185)
right_arm_motor.run_angle(350, -400, Stop.BRAKE, True)

#go backward to mission 3
<<<<<<< HEAD
drive_general(380, -350, 185, True)
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -100, Stop.BRAKE, True)
drive_general(500, 1000, 185, True)
turn_general(50, False)
drive_general(300, 1000, 50 , True)
=======
drive_general(780, -350, 93, True)

#put the scubadiver on the yellow line and click on the yellow
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -365, Stop.BRAKE, True)
drive_general(350, 400, 0, False)
turn_general(-90)
#drive straight to mission 6
drive_general(85, 150, 0, False)

#get up the toren
drive_general(160, 70, 0, False)

#take the srimp
right_arm_motor.run_angle(350, 450, Stop.BRAKE, True)

#take the chest
drive_general(100, -200, 0, False)
turn_general(120)
drive_general(440, 2000, 120, True)
>>>>>>> parent of c71121c (Update run3.py)
