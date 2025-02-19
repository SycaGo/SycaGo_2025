from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

#put the coral on the yellow
drive_general(280, 350, 0, False)
left_arm_motor.run_angle(320, -120, Stop.BRAKE,True)
drive_general(10, -165, 0, False)
wait(50)
left_arm_motor.run_angle(6000, -340, Stop.BRAKE,True)
drive_general(180, 350, 0, False)
turn_general(-10)
left_arm_motor.run_angle(50, 80, Stop.BRAKE,True)
left_arm_motor.run_angle(20, -80, Stop.BRAKE,True)
drive_general(100, -200, -10, True)

#free shark
turn_general(60)
drive_general(300, 350, 60, True)
turn_general(-10)
drive_general(200, 350, -10, True)
turn_general(-47)
drive_general(16, 500, -47, True)
left_arm_motor.run_angle(10000,700, Stop.BRAKE,True)
#corals and diver
drive_general(150, -350, -47, True)
left_arm_motor.run_angle(250, -600, Stop.BRAKE,False)
turn_general(-35, False)
drive_general(150, 350, -35, True)
right_arm_motor.run_angle(100, -200, Stop.BRAKE,True)
