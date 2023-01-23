from datetime import datetime

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
    for user in users:
        day = (user['birthday'].weekday())
    return(weekdays[day])

print (get_birthdays_per_week(users))