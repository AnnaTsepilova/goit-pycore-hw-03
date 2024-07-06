from datetime import datetime

def get_days_from_today(date):
    """
    Function return period in days between two entered date and current_date(now)
    """
    days = 0
    datetime_object = datetime.strptime(date, '%Y-%m-%d')
    print(datetime_object)

    current_date = datetime.today()
    print(current_date)

    days = current_date - datetime_object

    return days

data = input("Input date in format `YYYY-mm-dd`?\n")
delta_days = get_days_from_today(data)
print(delta_days)