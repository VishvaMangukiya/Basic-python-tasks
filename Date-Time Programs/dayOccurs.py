from datetime import date, timedelta

def count_weekdays_in_year(year):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)

    weekdays_count = {
        "Monday": 0, "Tuesday": 0, "Wednesday": 0,
        "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0
    }

    current_date = start_date
    while current_date <= end_date:
        weekday_name = current_date.strftime("%A")
        weekdays_count[weekday_name] += 1
        current_date += timedelta(days=1)

    return weekdays_count

year_input = int(input("Enter the year: "))
result = count_weekdays_in_year(year_input)
for day, count in result.items():
    print(f"{day}: {count}")
