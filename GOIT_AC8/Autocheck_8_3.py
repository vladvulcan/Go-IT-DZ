from datetime import datetime


def get_str_date(date):
    D = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    D = D.strftime('%A %d %B %Y')
    return (D)