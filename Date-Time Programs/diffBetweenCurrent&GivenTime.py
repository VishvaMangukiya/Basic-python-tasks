from datetime import datetime

now = datetime.now()

user_time = input("Enter time in HH:MM format: ")

given_time = datetime.strptime(user_time, "%H:%M")
given_time = given_time.replace(year=now.year, month=now.month, day=now.day)

diff = abs(now - given_time)
hours = diff.seconds // 3600
minutes = (diff.seconds % 3600) // 60

print("Time difference:", hours, "hours and", minutes, "minutes")
