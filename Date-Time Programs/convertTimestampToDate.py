from datetime import datetime

timestamp_str = "1754776800"

dt_obj = datetime.fromtimestamp(float(timestamp_str))

print("Datetime object:", dt_obj)
