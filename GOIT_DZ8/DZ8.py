from datetime import datetime, timedelta

current_date = datetime.now().date()

users = [
    {"name": 'Vladimir','birthday':datetime(year=1996,month=1,day=24)},
    {"name": 'Igor','birthday':datetime(year=1968,month=1,day=24)},
    {"name": 'Marianne','birthday':datetime(year=1967,month=1,day=25)},
    {"name": 'Diane','birthday':datetime(year=1967,month=1,day=26)},
    {"name": 'Ilya','birthday':datetime(year=2001,month=1,day=27)},
    {"name": 'Chloe','birthday':datetime(year=1994,month=1,day=28)},
    {"name": 'Max','birthday':datetime(year=1995,month=1,day=29)}
]

def get_birthdays_per_week(users,date=current_date):
    if isinstance(date,str):
        date = datetime.strptime(date,'%d %B %Y').date()
    one_week = timedelta(weeks=1)
    message = "Don't forget to congratulate on "
    start = len(message)
    bdays = {}
    for user in users:
        name = user['name']
        bd2023 = datetime(year=2023,month=user['birthday'].month,day=user['birthday'].day).date()
        to_birthday = bd2023-date
        if to_birthday <= one_week and to_birthday.days > 0:            
            bday = bd2023.strftime('%A')            
            if bday in ['Saturday','Sunday']:
                bday = 'Monday'
            
            names = []
            names.append(name)
            names_str = ', '.join(names)
            bdays[bday] = names_str
            
    for day, names in bdays.items():
        message += f'{day}: {names}\n'
            
    if len(message) > start:
        print(message)

    
# date = '14 october 2023'
get_birthdays_per_week(users)