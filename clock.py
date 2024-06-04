def calculate_clock_angle(hour, minute):
    if not (0 <= hour < 12) or not (0 <= minute < 60):
        return "Invalid input. Hour should be between 0 and 11, and minute should be between 0 and 59."

    hour_angle = (hour % 12) * 30 + (minute / 60) * 30
    minute_angle = minute * 6

    angle = abs(hour_angle - minute_angle)

    # If the angle is more than 180 degrees, subtract it from 360 to get the smaller angle
    if angle > 180:
        angle = 360 - angle

    return angle

hour = 10
minute = 00
result = calculate_clock_angle(hour, minute)
print(f"Angle between hour and minute hands at {hour}:{minute:02} is {result:.2f} degrees.")
