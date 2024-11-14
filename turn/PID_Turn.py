def turn(turn_degrees, Kp, Ki, Kd):

    hub.imu.reset_heading(0)
    
    error = turn_degrees - hub.imu.heading()
    integral = 0
    last_error = 0
    scale = abs(turn_degrees / 10)
    
    while abs(error) > 0.5:
        gyro = hub.imu.heading()
        error = turn_degrees - gyro
        p = error * Kp
        d = (error - last_error) * Kd
        correction = p + d
        if gyro >= abs(turn_degrees) - scale:
            integral += error
            i = integral * Ki
            correction = p + i + d
        last_error = error
        left_motor.run(correction)
        right_motor.run(-correction)
        
    left_motor.brake()
    right_motor.brake()
