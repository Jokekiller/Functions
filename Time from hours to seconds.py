#Harry Robinson
#14-12-2014
#Total number of seconds from hours etc

def time_details():
    hours = float(input("Enter the time in hours: "))
    minutes = float(input("Enter the minutes: "))
    seconds = float(input("Enter the seconds: "))
    return hours, minutes, seconds
def conversion(hours, minutes, seconds):
    hours_in_seconds = (hours * 60)* 60
    minutes_in_seconds = minutes * 60
    total_time = hours_in_seconds + minutes_in_seconds + seconds
    return total_time
#main
hours, minutes, seconds = time_details()
total_time = conversion(hours, minutes, seconds)
print(total_time)
