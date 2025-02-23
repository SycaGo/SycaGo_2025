from parameters import left_arm_motor, right_arm_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from drive_general import drive_general
from turn_general import turn_general

#run from the base to the coral
drive_general(280, 340, 0, False)

#catch the ring
left_arm_motor.run_angle(320, -350, Stop.BRAKE,True)

#take the coral
left_arm_motor.run_angle(6000, -380, Stop.BRAKE,False)
drive_general(30, -165, 0, True)

#put the coral on the rack
wait(50)
drive_general(165, 300, 0, True)
turn_general(20)

#exit from the rack after putting the coral
left_arm_motor.run_angle(6000, 320, Stop.BRAKE,True)
drive_general(40, -250, 20, True)

#drive to the next mission
turn_general(70)
drive_general(280, 350, 70, True)
turn_general(25)
drive_general(180, 350, 25, True)
turn_general(-48)
drive_general(140, 350, -48, True)

#free the shark
left_arm_motor.run_angle(10000, 750, Stop.BRAKE,True)

#go to mission 1
drive_general(140, -350, -48, True)
left_arm_motor.run_angle(6000, -820, Stop.BRAKE,True)
turn_general(-90)

#pushing the coral buds 
drive_general(130, 350, -90, True)
#take the diver
right_arm_motor.run_angle(6500, -450, Stop.BRAKE,True)
drive_general(110, -350, -90, True)
#return to the base
turn_general(-160)
drive_general(700, 650, -160, True)
