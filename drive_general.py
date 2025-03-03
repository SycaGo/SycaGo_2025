from parameters import left_motor, right_motor, hub, drive_base, WHEEL_DIAMETER
from pybricks.parameters import Stop
from pybricks.tools import wait


def calculate_distance():
    PI = 3.141592
    right_motor_angle = right_motor.angle()
    left_motor_angle = left_motor.angle()
    P = WHEEL_DIAMETER * PI
    average_angle = (abs(right_motor_angle) + abs(left_motor_angle)) / 2
    distance_driven = ((average_angle / 360) * P)
    return distance_driven

def drive_general(distance, speed, direction_angle, absolute=True, kp = 0.7, kd = 2):
    # distance is in millimeters
    # speed is in degrees (rotations) per second
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    last_error = 0
    if not(absolute):
        hub.imu.reset_heading(0)

    distance_passed = calculate_distance()
    final_speed = speed / 3

    deceleration_starting_position = (distance / 3)*2
    deceleration_range = distance - deceleration_starting_position
    max_speed = speed

    while distance_passed < distance:
        if distance > 150 or speed != 1000 or speed != -1000:
            if distance_passed > deceleration_starting_position:
                speed = (final_speed - max_speed) * ((distance_passed - deceleration_starting_position) / deceleration_range) + max_speed
        else:
            speed = max_speed
        distance_passed = calculate_distance()
        error = direction_angle - hub.imu.heading()
        p = error * kp
        d = (error - last_error) * kd
        correction = p + d            
        
        drive_base.drive(speed, correction)
    left_motor.brake()
    right_motor.brake()
    wait(100)
