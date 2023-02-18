def add_time(start, duration, *day):
  days_of_week = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday",
    "Saturday"
  ]

  start_time = start.split(" ")
  [start_time_clock, start_time_meridiem] = [start_time[0], start_time[1]]
  [start_time_hour, start_time_minutes
   ] = [start_time_clock.split(":")[0],
        start_time_clock.split(":")[1]]
  [duration_hour,
   duration_minutes] = [duration.split(":")[0],
                        duration.split(":")[1]]

  total_hours = int(start_time_hour) + int(duration_hour)
  total_minutes = int(start_time_minutes) + int(duration_minutes)
  no_of_days = 0

  if (total_minutes > 60):
    total_minutes -= 60
    total_hours += 1

  if total_minutes < 10:
    total_minutes = f"{total_minutes}".zfill(2)

  if total_hours >= 12:
    [t, r] = divmod(total_hours, 12)
    total_hours = r if r else total_hours - ((t - 1) * 12)

    if start_time_meridiem == "PM":
      no_of_days = (t // 2) + 1
    else:
      no_of_days = t // 2

    if t > 0 and t % 2 != 0:
      start_time_meridiem = "AM" if start_time_meridiem == "PM" else "PM"

  new_time = str(total_hours)
  new_time += ":" + str(total_minutes) + f" {start_time_meridiem}"

  if day:
    i = day[0].title()

    index = days_of_week.index(i)

    index += no_of_days

    if index >= len(days_of_week):
      index = index % 7

    i = days_of_week[index]

    new_time += ", " + i

  if no_of_days == 1:
    new_time += " (next day)"
  elif no_of_days > 1:
    new_time += f" ({no_of_days} days later)"

  return new_time


#print(add_time("3:00 PM", "3:10"))
#print(add_time("11:30 AM", "2:32", "Monday"))
#print(add_time("11:43 PM", "24:20", "tueSday"))
#print(add_time("2:59 AM", "24:00", "saturDay"))
