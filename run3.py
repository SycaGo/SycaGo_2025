from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

#get out of the launch area
drive_general(120, 350, 0, False)
turn_general(-90)
wait(100)

#drive straight to the Toren
drive_general(420, 350, -90, True)

#turn to alllign with the Toren
turn_general(90, False, Kp= 6)
wait(100)

#get up the toren
drive_general(180, 110, 90, True)
drive_general(80, 50, 90, True)

#take the srimp/ krill
right_arm_motor.run_angle(350, 430, Stop.BRAKE, True)

#take the chest
drive_general(180, -350, 90, True)

# release the shrimp in launch area
turn_general(185)
wait(500)
right_arm_motor.run_angle(350, -400, Stop.BRAKE, True)

#go backwards to the coral reef and the scuba diver hanger
drive_general(380, -350, 185, True)

# put the Scuba diver in the hanger and put down the coral reef
left_arm_motor.run_angle(10000, 1000, Stop.BRAKE, True)
left_arm_motor.run_angle(10000, -200, Stop.BRAKE, True)

#get back to launch area
drive_general(500, 1000, 185, True)
turn_general(50, False)
drive_general(300, 1000, 50, True)
