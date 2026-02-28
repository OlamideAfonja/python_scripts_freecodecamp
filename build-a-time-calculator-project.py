def add_time(start, duration, starting_day=None):
    # Split start time components
    time_part, period = start.split()
    start_hour, start_min = map(int, time_part.split(':'))
    
    # Split duration components
    dur_hour, dur_min = map(int, duration.split(':'))

    # Convert start hour to 24-hour format for calculation
    if period == "PM":
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Calculate total minutes
    total_mins = (start_hour * 60) + start_min + (dur_hour * 60) + dur_min
    
    # Calculate final components
    final_mins = total_mins % 60
    total_hours = total_mins // 60
    final_hour_24 = total_hours % 24
    days_later = total_hours // 24

    # Convert back to 12-hour format
    final_period = "AM" if final_hour_24 < 12 else "PM"
    
    final_hour_12 = final_hour_24 % 12
    if final_hour_12 == 0:
        final_hour_12 = 12

    # Formatting time string
    new_time = f"{final_hour_12}:{final_mins:02d} {final_period}"

    # Handle optional Day of the Week
    if starting_day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days.index(starting_day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_time += f", {days[new_day_index]}"

    # Handle Day notation
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


