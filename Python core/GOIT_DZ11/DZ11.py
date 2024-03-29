from collections import UserDict
from datetime import datetime, timedelta
import re

def input_error(func):
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res

        except KeyError:
            return "No such name"
        
        except ValueError as err:
            return err.args[0]

        except IndexError:
            return 'Name is given, but phone number is not'
        
        except TypeError:
            return "Give me name and phone please"

    return inner


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):

    @Field.value.setter
    def value(self, name):        
        if not name.isalpha():
            raise ValueError('Name must be a text, not number')
        self._value = name



class Phone(Field):

    @Field.value.setter
    def value(self, new_phone):
        pattern = r"\+\d{3}-\d{3}-\d{2}-\d{2}"
        if not re.match(pattern, new_phone):
            raise ValueError('The phone must be in +111-222-33-44 format')
        self._value = new_phone


class Birthday(Field):
    
    @Field.value.setter
    def value(self, birthday):
        try:
            self._value = datetime.strptime(birthday, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid birthdate format. The date needs to be in YYYY-mm-dd format")


class Record:
    def __init__(self, name, phone = None, birthday = None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.add_phone(phone)
        if birthday:
            self.birthday = Birthday(birthday)

    def __repr__(self):
        return f'{self.name.value}, phones: {", ".join([phone.value for phone in self.phones])}'

    def add_phone(self, phone): 
       self.phones.append(Phone(phone))
       

    def clear_phones(self): 
        self.phones.clear()

    def delete_phone(self, index):
        self.phones.pop(index)

    def find_phone(self, phone):
        index = next((i for i, p in enumerate(self.phones) if p.value == phone), -1)
        return index >= 0, index


    
    def days_to_birthday(self):
        curdate = datetime.today().date()
        next_birthday_year = curdate.year
        self.next_bd = datetime(next_birthday_year, self.birthday.value.month, self.birthday.value.day).date()
        days_to_birthday =  (self.next_bd - curdate).days
        if days_to_birthday < 0:
            next_birthday_year += 1
            self.next_bd = datetime(next_birthday_year, self.birthday.value.month, self.birthday.value.day).date()
            days_to_birthday += 365
        return days_to_birthday


        

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def update_record(self,name,phone):
       self.data[name].add_phone(phone)

    def get_phones(self,name):
        return [phone.value for phone in self.data[name].phones]
    
    def remove_record(self, name):
        del self.data[name]
    
    def clear_phones(self, name):
        self.data[name].clear_phones()

    def delete_phone(self, name, phone):
        number, index = self.data[name].find_phone(phone)
        if number:
            self.data[name].delete_phone(index)


    def iterator(self, num_iterations=5):        
        result = []
        i = 0

        for record in self.data.values():
            result.append(record)
            i += 1

            if i == num_iterations:
                yield result
                result = []
                i = 0

        if result:
            yield result
            


 
   
memory = AddressBook({'v': Record('v','+111-222-33-44','1996-03-12')})

def calculate_days_to_birthday(name):
    name = name[1:]
    return memory[name].days_to_birthday()

def get_birthday(name):
    name = name[1:]
    return memory[name].birthday.value

def say_hello(): 
    return 'How can I help you?'

def say_goodbye():
    return 'Good bye!'

def show_help():
    help = '''
Список доступных команд:
"hello" - бот отвечает "How can I help you?"
"add ..." -   бот сохраняет в памяти новый контакт. Вместо ... введите имя и номер телефона через пробел.
"change ..." - бот сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... введите имя и номер телефона.
"phone ..." - бот выводит в консоль номер телефона для указанного контакта. Вместо ... введите имя пользователя через пробел.
"show all" - бот выводит все сохраненные контакты с номерами телефонов в консоль в формате "Имя: телефон".
"goodbye", "close", "exit" - бот пишет "Good bye!" и завершает свою работу.
'''
    return help


@input_error
def add_new_user(command: str):
    userdata = command[1:].split()
    if len(userdata) ==3:
        name, phone, bd = userdata[0], userdata[1], userdata[2]
        new_user = Record(name, phone, bd)
    elif len(userdata) ==2:
        name, phone = userdata[0], userdata[1]
        new_user = Record(name, phone)
    else:
        raise IndexError

    if new_user.name.value in memory:
        raise ValueError(f'This name already exists.\nType "phone {userdata[0]}" to see the number linked to it.')    
    else:       
        memory.add_record(new_user)
    message = f'Added to memory: Name - {userdata[0]}, phone - {userdata[1]}'
    return message
    
@input_error
def update_user(command: str):
    name_phone = command[1:].split()
    name, new_phone_number = name_phone[0], name_phone[1]    
    memory.update_record(name, new_phone_number)
    message = f'Changed in memory: Name - {name}, new phone - {new_phone_number}'
    return message

@input_error
def clear_user(command: str):
    name = command[1:]
    confirm = input(f'This will delete all the phones for existing user {name}. Proceed? (Y/N)\n')
    if confirm.lower() == 'y':
        memory.clear_phones(name)
        message = f'User "{name}" cleared successfully'
    else:
        message = "Action is aborted"
    return message


@input_error
def get_users_phone(command: str):
    name = command[1:]
    return memory.get_phones(name)

@input_error
def get_database(cmd):
    num_iterations = cmd[1:]
    if num_iterations == 'all':
        return [i for i in memory.data.values()]

    else:
        num_iterations = int(num_iterations)        
        for res in memory.iterator(num_iterations):
            return res


@input_error
def delete_user(command: str):
    name = command[1:]
    confirm = input(f'This will delete the user {name}. Proceed? (Y/N)\n')
    if confirm.lower() == 'y':
        memory.remove_record(name)
        message = f'User "{name}" deleted successfully'
    else:
        message = "Action is aborted"
    return message

@input_error
def delete_phone(command: str):
    name_phone = command[1:].split()
    name, phone_number = name_phone[0], name_phone[1]
    memory.delete_phone(name, phone_number)
    return "Phone deleted successfully"


    



COMMANDS_DICT = {
    'help': show_help,
    'hello': say_hello,
    'exit': say_goodbye,
    'close': say_goodbye,
    'good bye': say_goodbye,
    'stop': say_goodbye,
    'add': add_new_user,
    'change': update_user,
    'phone': get_users_phone,
    'show': get_database,
    'clear': clear_user,
    'delete': delete_user,
    'del phone': delete_phone,
    'bd': calculate_days_to_birthday,
    'date': get_birthday
}


def command_selector(command):
    return COMMANDS_DICT[command]

def parser(user_input: str):
    for key in COMMANDS_DICT:
        if user_input.lower().startswith(key):
            action = command_selector(key)
            data = user_input.removeprefix(key)
            if data:
                return action(data)
            else:
                return action()
    error_message = 'Invalid command. Try again.\nFor the list of available commands type "help"'
    return error_message
                

def main():
    while True:
        user_input = input('enter command: ')
        if user_input == '.':
            break
        result = parser(user_input)
        if user_input == 'phone' and result == 'Give me name and phone please':
            result = 'Give me name please'
        print (result)
        if result == 'Good bye!':
            break        
    


if __name__ == '__main__':
    main()
    
