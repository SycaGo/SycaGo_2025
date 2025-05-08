from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general
from white_stop import white_stop   

# this run completes the missions:12,10,5

# driving from the launch area to the whale, drops the shrimps
drive_general(100, 350, 0, False)
turn_general(-27)
drive_general(500, 400, -27, True)
turn_general(44, Kp=7)
drive_general(330, 200, 44, True)
wait(500)
drive_general(20, -200, 44, True)
drive_general(50, 400, 44, True)
wait(500)

#leave the reef segments behind
left_arm_motor.run_angle(3000, 1000, Stop.BRAKE,True)


# pushing the fish
drive_general(270, -300, 44, True)
turn_general(-51, Kp=7)
drive_general(170, 500, -51, True)

# lifting the shered mission
turn_general(-90, Kp=7)

drive_general(250, 500, -90, True)
turn_general(-113, Kp=7)
drive_general(150, 500, -113, True)
drive_general(100, -500, -113, True)
turn_general(-70)
white_stop(100)
right_arm_motor.run_angle(10000, -850, Stop.BRAKE, True)
wait(1000)

# place the unidentifled creature
drive_general(30, -300, 20, True)
