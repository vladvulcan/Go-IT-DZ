from datetime import datetime, timedelta

current_date = datetime.now().date()
one_week = timedelta(weeks=1)
next_date = current_date + one_week
timediff = next_date - current_date

users = [
    {"name": 'Vladimir','birthday':datetime(year=1996,month=7,day=12)},
    {"name": 'Igor','birthday':datetime(year=1968,month=11,day=1)},
    {"name": 'Marianne','birthday':datetime(year=1967,month=10,day=16)},
    {"name": 'Ilya','birthday':datetime(year=2001,month=1,day=27)},
    {"name": 'Chloe','birthday':datetime(year=1994,month=3,day=11)},
    {"name": 'Max','birthday':datetime(year=1995,month=9,day=21)}
]

def get_birthdays_per_week(users):
    weekdays = {0: 'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    users_by_day = []
    for user in users:
        name = user['name']
        bd2023 = datetime(year=2023,month=user['birthday'].month,day=user['birthday'].day).date()
        to_birthday = bd2023-current_date
        if to_birthday <= timediff:
            bday = bd2023.weekday()
            bday = weekdays[bday]
            print(f'{name}: {bday}')

    

    

get_birthdays_per_week(users)