from parameters import drive_base, hub, right_motor, left_motor
def turn(set_point, Kp, Ki, Kd):
    hub.imu.heading(0)
    current_point = hub.imu.heading()
    error = set_point - current_point
    integral = 0
    last_error = 0
    while abs(error)>0.5:
        current_point = hub.imu.heading()
        error = set_point - current_point
        p = error * Kp
        d = (error - last_error) * Kd
        correction = p + d
        if  current_point >= abs(set_point) - scale:
            integral += error
            i = integral * Ki
            correction = p + i + d
        last_error = error
        right_motor(correction)
        left_motor(-correction)
    left_motor.brake()
    right_motor.brake()
