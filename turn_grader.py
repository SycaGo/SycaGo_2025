from parameters import drive_base, right_motor, left_motor, hub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop

def turn(turn_degrees, Kp, Ki, Kd):
    global goal_degrees
    global turn_Kp
    global turn_Ki
    global turn_Kd
    goal_degrees = turn_degrees
    turn_Kp = Kp
    turn_Kd = Kd
    turn_Ki = Ki

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
            correction = p + d + i
        last_error = error
        left_motor.run(correction)
        right_motor.run(-correction)
    left_motor.brake()
    right_motor.brake()

def grader(wanted_angle, Kp, Ki, Kd):
    global total_score

    masured_angle = hub.imu.heading()
    angle_max_score = 40

    overshoot_max_score = 5

    masured_time = float(timer.time())
    time_max_score = 25

    Kp_max_score = 10

    Ki_max_score = 10

    Kd_max_score = 10
    

    overshoot = wanted_angle - masured_angle


    if 0 > overshoot > -1:
        overshoot_coefficient = (1 - abs(overshoot)) * 1
        if overshoot_coefficient > 1:
            overshoot_coefficient = 1
        overshoot_score = overshoot_max_score * overshoot_coefficient
    elif -1 >= overshoot >= 2.5:
        overshoot_coefficient = abs(1 - (overshoot_coefficient / 3))
        overshoot_score = overshoot_max_score * overshoot_coefficient
    else:
        overshoot_coefficient = 1
        overshoot_score = overshoot_max_score * overshoot_coefficient

    max_error = 5
    angle_left = min(max_error, abs(wanted_angle - masured_angle))

    if angle_left < 1:
        error_grader_coefficient = 1
    else:
        error_grader_coefficient = (angle_left - 1) * (-1 / max_error) + 1

    angle_score = angle_max_score * error_grader_coefficient
    

    masured_time = masured_time / 1000
    if masured_time < 2:
        time_coefficient = (masured_time - 1) * (-1 / max_error) + 1
    else:
        time_coefficient = 0

    time_score = time_max_score * time_coefficient


    if 3 <= Kp < 10:
        Kp_score = Kp_max_score
    else:
        Kp_score = 0
        

    if 0 <= Ki < 1:
        Ki_score = Ki_max_score
    else:
        Ki_score = 0


    if 1 <= Kd <= 3:
        Kd_score = Kd_max_score
    else:
        Kd_score = 0


    total_score = angle_score + time_score + Kp_score + Ki_score + Kd_score + overshoot_score

    
    print(f"Your score for the angle is {angle_score}")
    print(f"Your score for the time is {time_score, 2}")
    print(f"Your score for the Kp is {Kp_score}")
    print(f"Your score for the Ki is {Ki_score}")
    print(f"Your score for the Kd is {Kd_score}")
    print(f"Your score for the overshoot is {overshoot_score}")
    print(f"Your total score is {total_score}")


timer = StopWatch()

repetation = 3

average_score = 0
for activation in range(repetation):
    timer.reset()
    timer.resume()
    turn(-60, 9, 0.003, 2)
    grader(goal_degrees, turn_Kp, turn_Ki, turn_Kd)
    average_score += total_score
    wait(1000)

average_score = average_score / repetation

print(f"\nThe average score is {average_score}\n")

if average_score > 80:
    print("Excellent turn!\n")
else:
    print("Keep calibrating\n")
