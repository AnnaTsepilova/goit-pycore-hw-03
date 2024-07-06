from datetime import datetime

def get_days_from_today(date):
    """
    Function return period in days between entered date and current_date(now)
    """
    try:
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date")
        return False

    current_date = datetime.today()

    time_delta = current_date - datetime_object

    return time_delta.days

data = input("Input date in format `YYYY-MM-DD`?\n")
delta_days = get_days_from_today(data)
print(delta_days)
