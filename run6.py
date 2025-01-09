from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take shrimps and coral
drive_general(100, 400, 0, False)
turn_general(-30)
right_arm_motor.run_angle(800, 2000, Stop.BRAKE, False)
drive_general(250, 400, -30, True)
turn_general(15)
drive_general(300, 400, 15, True)

#mini ship
turn_general(-20)
drive_general(100, -200, -20, True)
right_arm_motor.run_angle(-5000, 1000, Stop.BRAKE)

#mission 13
drive_general(70, 400, 0, False)
turn_general(40)
drive_general(150, 400, 40, True)
left_arm_motor.run_angle(5000, 1000, Stop.BRAKE, False)
turn_general(60)
left_arm_motor.run_angle(5000, 1000, Stop.BRAKE, False)


'''
turn_general(90)
drive_general(150, 400, 90, True)









#octupos
drive_general(420, 400, 0, False)

#take shrimps and coral
drive_general(100, -400, 0, False)
left_arm_motor.run_angle(-300, 300, Stop.BRAKE, True)
turn_general(40)
drive_general(500, 400, 42, True)

#mini ship
turn_general(-32)
drive_general(100, -200, 0, False)
right_arm_motor.run_angle(-5000, 1000, Stop.BRAKE)


#mission 13
turn_general(-30)
drive_general(40, -400, -30, True)
left_arm_motor.run_angle(200, 295, Stop.BRAKE, True)
drive_general(50, -400, -30, True)
left_arm_motor.run_angle(200,-295, Stop.BRAKE, True)
drive_general(70, 400, -30, True)


drive_general(200, 400, 0, False)
turn_general(45)
drive_general(520, 400, 45, True)
turn_general(-30)
drive_general(100, -400, -30, True)
right_arm_motor.run_angle(-5000, 1000, Stop.BRAKE)
drive_general(100, 400, -30, True)
left_arm_motor.run_angle(800, 260, Stop.BRAKE, True)
turn_general(28)
drive_general(200, 400, 28, True)
turn_general(20)
'''
