from datetime import datetime

now = datetime.now()

formatted = now.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", formatted)
