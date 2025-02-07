from parameters import left_motor, right_motor, right_color_sensor, left_color_sensor, hub, drive_base, WHEEL_DIAMETER
from pybricks.parameters import Stop
from pybricks.tools import wait

def white_stop(speed):
    hub.imu.reset_heading(0)
    set_point = 0
    GOAL_REFLECTION = 90
    left_motor_reflection= left_color_sensor.reflection()
    kp = 0.7
    kd = 2
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    last_error = 0
    right_motor_stop = False
    while right_motor_stop == False:
        right_motor_reflection = right_color_sensor.reflection()
        if left_motor_reflection < GOAL_REFLECTION+10:
            left_motor_reflection = left_color_sensor.reflection()
            error = set_point - hub.imu.heading()
            p = error * kp
            d = (error - last_error) * kd
            correction = p + d
            drive_base.drive(speed, correction)
        if GOAL_REFLECTION -10 < right_motor_reflection < GOAL_REFLECTION +10:
            right_motor_stop = True
            right_motor.brake()
            left_motor.brake()
