#Experimental stuff here for personal use
from datetime import datetime, timedelta

current_date = datetime.now().date()

users = [
    {"name": 'Vladimir','birthday':datetime(year=1996,month=1,day=23)},
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
    names = []
    count = 1
    for user in users:        
        next_bd = datetime(year=date.year,month=user['birthday'].month,day=user['birthday'].day).date()
        to_birthday = next_bd-date
        if to_birthday <= one_week and to_birthday.days > 0:
            name = user['name']            
            bday = next_bd.strftime('%A')            
            if bday in ['Saturday','Sunday']:
                bday = 'Monday'          
                        
            if bday in bdays:
                count += 1
            else:
                count = 1
                names.clear()
            if count >1:
                if not names:
                    names.append(bdays[bday])
                names.append(name)
                bdays[bday] = ', '.join(names)
            else:
                bdays[bday] = name
            
    for day, names in bdays.items(): 
        message += f'{day}: {names}\n'
            
    if len(message) > start:
        print(message)

    
date = '22 January 2024'
get_birthdays_per_week(users,date)