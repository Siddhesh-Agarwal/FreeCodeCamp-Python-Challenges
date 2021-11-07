class Time:
    def __init__(self, time_string):
        time_string = time_string.replace(' ', ':')
        time_string = time_string.split(':')
        self.hours = int(time_string[0])
        self.minutes = int(time_string[1])
        if len(time_string) == 3:
            self.time_zone = time_string[2]
            self.hours += 12 if self.time_zone == "PM" else 0

    def __add__(self, duration):
        days = duration.hours // 24
        duration.hours %= 24
        end_minutes = self.minutes + duration.minutes
        end_hours = self.hours + duration.hours
        end_hours += end_minutes // 60
        end_minutes %= 60
        days += end_hours // 24
        end_hours %= 24
        end_time_zone = ["AM", "PM"][end_hours // 12]
        end_hours %= 12
        if end_minutes < 10:
            end_minutes = "0" + str(end_minutes)
        if end_hours == 0: # 0 hours to be changed to 12 hours
            end_hours = 12
        
        string = f"{end_hours}:{end_minutes} {end_time_zone}"
        if days == 1:
            string += " (next day)"
        elif days > 1:
            string += f" ({days} days later)"
        return string

def add_time(start, duration, weekday=None):
    new_time = Time(start) + Time(duration)
    weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if weekday != None:
        weekday = weekday.title()        # To avoid case sensitivity
        new_time = new_time.split()      # Split the string into a list
        try:
            end_days = new_time[2][1:]   # remove the first character (the '(')
            if end_days == "next":       # Changes next day to 1 day
                end_days = "1"
        except IndexError:               # occurs when the end_days is 0 and hence not returned
            end_days = "0"
        end_weekday = weekday_list[(weekday_list.index(weekday) + int(end_days)) % 7]
        new_time = f"{new_time[0]} {new_time[1]}, {end_weekday} {' '.join(new_time[2:])}"
    return new_time.rstrip()