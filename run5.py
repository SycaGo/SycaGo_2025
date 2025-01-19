from parameters import left_arm_motor, right_arm_motor,hub,drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait
from turn_general import turn_general
from drive_general import drive_general

#take shrimps and coral
drive_general(100, 250, 0, False)
turn_general(-36)
drive_general(150, 250, -36, True)
turn_general(35)
left_arm_motor.run_angle(300, 400, Stop.BRAKE, False)
drive_general(500, 500, 35, True)
print(hub.imu.heading())

#mission 13
drive_general(10, -200, 35, True)
turn_general(25)
drive_general(200, -400, 25, True)

# take shrimp and Plankton Sample
turn_general(35)
left_arm_motor.run_angle(300, -500, Stop.BRAKE, True)
drive_general(120, 400, 35, True)
turn_general(25)
drive_general(20, 250, 25, True)
left_arm_motor.run_angle(300, 500, Stop.BRAKE, True)
drive_general(20, -400, 25, True)

#octupos
turn_general(-70)
drive_general(400, -500, -90, True)
turn_general(-40)
drive_general(200, 500, -40, True)
drive_general(570, -600, 0, False)
  
