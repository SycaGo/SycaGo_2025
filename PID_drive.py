from parameters import drive_base, hub, right_motor, left_motor, WHEEL_DIAMETER
from pybricks.tools import wait

def calculate_distance():
    right_motor_angle = right_motor.angle()
    left_motor_angle = left_motor.angle()
    P = WHEEL_DIAMETER * 3.14192
    average_angle = (abs(right_motor_angle) + abs(left_motor_angle)) / 2
    distance_driven = ((average_angle / 360) * P) / 10
    return distance_driven

def drive(kp, ki, kd, set_point, speed, distance):
    integral = 0
    last_error = 0
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    hub.imu.reset_heading(0)

    scale = abs(set_point / 10)
    distance_passed = calculate_distance()
    
    final_speed = 30
    deceleration_starting_position = (distance / 3) * 2
    deceleration_range = distance - deceleration_starting_position
    max_speed = speed
    while distance_passed < distance:
        distance_passed = calculate_distance()
        error = set_point - hub.imu.heading()
        p = error * kp
        d = (error - last_error) * kd
        correction = p + d
        
        if abs(hub.imu.heading()) >= (abs(set_point) - scale):
            integral += error
            i = integral * ki
            correction = p + i + d
            
        last_error = error

        if distance_passed < deceleration_starting_position:
            speed = max_speed
        else:
            speed = (final_speed - max_speed) * ((distance_passed - deceleration_starting_position) / deceleration_range) + max_speed
        
        drive_base.drive(speed, correction)


    left_motor.brake()
    right_motor.brake()

    wait(100)
