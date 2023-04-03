from datetime import datetime


def get_days_from_today(date):
    current_date = datetime.now().date()
    new_date = datetime.strptime(date, '%Y-%m-%d' ).date()
    return (current_date-new_date).days