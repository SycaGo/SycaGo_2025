from parameters import left_motor, right_motor, hub, drive_base
from pybricks.parameters import Stop
from pybricks.tools import wait

def turn_general(turn_degrees, Kp = 8, Ki = 0.009, Kd = 2):
    error = turn_degrees - hub.imu.heading()
    integral = 0
    last_error = 0
    while abs(error) > 0.5:
        gyro = hub.imu.heading()
        error = turn_degrees - gyro
        p = error * Kp
        d = (error - last_error) * Kd
        integral += error
        correction = p + d

        if abs(error) > 5:
            integral = 0
        elif abs(error) <= 5:
            i = integral * Ki
            correction = p + i + d
        last_error = error
        left_motor.run(correction)
        right_motor.run(-correction)
    left_motor.brake()
    right_motor.brake()
