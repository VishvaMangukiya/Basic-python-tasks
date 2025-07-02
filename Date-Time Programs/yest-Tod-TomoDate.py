from datetime import date, timedelta

today = date.today()

yesterday = today - timedelta(days=1)

tomorrow = today + timedelta(days=1)

print("Yesterday's Date :", yesterday)
print("Today's Date     :", today)
print("Tomorrow's Date  :", tomorrow)
