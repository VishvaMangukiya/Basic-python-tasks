from datetime import datetime

date_str = "2025-08-11 10:30:00"

dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

timestamp = dt_obj.timestamp()

print("Timestamp:", timestamp)

