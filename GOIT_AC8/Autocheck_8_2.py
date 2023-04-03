from datetime import date, datetime


def get_days_in_month(month, year):
    MY = f"{month} {year}"
    if month != 12:
        next_month = f"{month+1} {year}"
    else:
        next_month = f"{1} {year+1}"
    MY = datetime.strptime(MY, '%m %Y').date()
    next_month = datetime.strptime(next_month, '%m %Y').date()
    days = next_month-MY
    return (days.days)