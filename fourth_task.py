from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users: list) -> list:
    """
    Function return upcomming birthdays.
    """
    birthdays = []

    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Birthday this year
        if birthday.month >= today.month and birthday.day >= today.day:
            specific_date = datetime(year=today.year, month=birthday.month, day=birthday.day).date()
        # Birthday next year
        else:
            specific_date = datetime(year=today.year + 1, month=birthday.month, day=birthday.day).date()

        ## Birthday next 7 days
        if (specific_date - today).days <= 7:
            weekend_correction = 0
            if specific_date.isoweekday() > 5:
                weekend_correction = 7 - specific_date.isoweekday() + 1

            congratulation_date = specific_date + timedelta(days=weekend_correction)
            birthdays.append(
                {
                    'name': user["name"],
                    'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
                }
            )

    return birthdays



users = [
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
