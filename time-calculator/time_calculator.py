def add_time(start, duration, day=""):

    days = [
        "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
        "sunday"
    ]

    #seperate the time and period.
    time = start.split(" ")[0]
    period = start.split(" ")[1]

    #create the period options.
    if period == "AM":
        second_period = "PM"
    else:
        second_period = "AM"

    #seperate the time as hour and minute.
    hour = time.split(":")[0]
    minute = time.split(":")[1]

    #seperate the added duration as hour and minute.
    add_hour = duration.split(":")[0]
    add_minute = duration.split(":")[1]

    #checking the minute is less than 60.
    if int(minute) > 59 or int(add_minute) > 59:
        return "Error: Minutes must be less than 60."

    hour_increase = int(add_hour) + ((int(minute) + int(add_minute)) // 60)

    #calculate the new hour.
    new_hour = (int(hour) + hour_increase) % 12
    if new_hour == 0:
        new_hour = 12

    #calculate the new period.
    new_period = period
    to_period_change = 12 - int(hour)
    if hour_increase % 12 >= to_period_change:
        if ((hour_increase - to_period_change) % 24) < 12:
            new_period = second_period

    #calculate the new minute.
    new_minute = (int(minute) + int(add_minute)) % 60
    if new_minute < 10:
        new_minute = f"0{new_minute}"

    #calculate the passed day.
    if period == "AM":
        passed_day = abs((int(hour) + hour_increase)) // 24
    else:
        passed_day = abs((int(hour) + hour_increase) + 12) // 24

    #calculate the new day.
    if day:
        day_index = days.index(day.lower())
        new_day = days[int(day_index + (passed_day % 7)) % 7]
        new_day = new_day.capitalize()

    #clean up the passed day output.
    if passed_day == 0:
        passed_day = ""
    elif passed_day == 1:
        passed_day = " (next day)"
    else:
        passed_day = f" ({passed_day} days later)"

    #constructing the final output.
    if day:
        return f"{new_hour}:{new_minute} {new_period}, {new_day}{passed_day}"
      
    else:
        return f"{new_hour}:{new_minute} {new_period}{passed_day}"
