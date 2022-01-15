def add_time(start, duration, day=None):
    new_time, period = '', ''
    oh, om, dh, dm, h, m = 0, 0, 0, 0, 0, 0

    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Get hours, minutes and period
    oh = int(start.split()[0].split(":")[0])
    om = int(start.split()[0].split(":")[1])
    period = start.split()[1]

    dh = int(duration.split(":")[0])
    dm = int(duration.split(":")[1])

    # 12h to 24h
    if period == 'AM':
        h = oh + dh
    elif period == 'PM':
        h = oh + dh + 12

    m = om + dm

    # Formating minutes
    if m > 59:
        m -= 60
        h += 1

    # Days
    days = h // 24
    h -= 24 * days

    # Formating hours
    if not days and h >= 12 and period == 'AM':
        h -= 12
        period = 'PM'
    elif period == 'PM' and h >= 24:
        h -= 12
        period = 'AM'
        days = 1
    elif h > 12:
        period = 'PM'
        h -= 12
    else:
        period = 'AM'

    # Special case
    if h == 0:
        h = 12

    # Prints
    if 0 <= m < 10:
        new_time = f'{h}:0{m} {period}'
    else:
        new_time = f'{h}:{m} {period}'

    # Week day
    if day:
        i = week.index(day.capitalize())
        newd = week[(i + days) % 7]
        new_time += f', {newd}'

    if days:
        if days > 1:
            new_time += f' ({days} days later)'
        else:
            new_time += ' (next day)'

    return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
print(add_time("8:16 PM", "466:02", "tuesday"))
