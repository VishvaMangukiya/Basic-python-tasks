def convert_to_24(time_str):
    from datetime import datetime

    in_time = datetime.strptime(time_str, "%I:%M %p")

    out_time = in_time.strftime("%H:%M")

    return out_time

time_12hr = input("Enter time in 12-hour formate (e.g., 03:30 PM): ")
time_24hr = convert_to_24(time_12hr)
print("24-hour format: ",time_24hr)