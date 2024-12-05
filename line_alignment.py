from parameters import right_color_sensor, left_color_sensor, drive_base, left_motor, right_motor

def line_alignment(speed):
    left_motor_stop = False
    right_motor_stop = False
    GOAL_REFLECTION = 90
    right_motor.run(speed)
    left_motor.run(speed)
    while right_motor_stop == False or left_motor_stop == False:
        right_motor_reflection = right_color_sensor.reflection()
        left_motor_reflection = left_color_sensor.reflection()
        if GOAL_REFLECTION -10 < right_motor_reflection < GOAL_REFLECTION +10:
            right_motor_stop = True
            right_motor.stop()
        if GOAL_REFLECTION -10 < left_motor_reflection < GOAL_REFLECTION +10:
            left_motor_stop = True
            left_motor.stop()
