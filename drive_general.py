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

def drive_general(distance_mm, speed_deg_s, direction_angle, absolute=True, kp = 0.7, kd = 2):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    last_error = 0
    if not(absolute):
        hub.imu.reset_heading(0)

    distance_passed = calculate_distance()
    final_speed = speed_deg_s / 3

    deceleration_starting_position = (distance_mm / 3)*2
    deceleration_range = distance_mm - deceleration_starting_position
    max_speed = speed_deg_s

    while distance_passed < distance_mm:
        if distance_mm > 150 or speed_deg_s != 1000 or speed_deg_s != -1000:
            if distance_passed > deceleration_starting_position:
                speed_deg_s = (final_speed - max_speed) * ((distance_passed - deceleration_starting_position) / deceleration_range) + max_speed
        else:
            speed_deg_s = max_speed
        distance_passed = calculate_distance()
        error = direction_angle - hub.imu.heading()
        p = error * kp
        d = (error - last_error) * kd
        correction = p + d            
        
        drive_base.drive(speed_deg_s, correction)
    left_motor.brake()
    right_motor.brake()
    wait(100)
