from collections import UserDict
from datetime import datetime, timedelta
import re
import pickle


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
    
    def search_in_phones(self, query):
        for phone_obj in self.phones:
            return query in phone_obj.value

       

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
            
def read_from_backup():
    backup_file = r'GOIT_DZ12\backup.bin'
    with open(backup_file, "rb") as bf:
        memory = pickle.load(bf)
        return memory

 
try:
    memory = read_from_backup()
except FileNotFoundError:
    memory = AddressBook({'Vova': Record('Vova','+111-222-33-44','1996-03-12')})

def calculate_days_to_birthday(name):
    return memory[name].days_to_birthday()

def get_birthday(name):
    return memory[name].birthday.value

def say_hello(): 
    return 'How can I help you?'

def say_goodbye():
    return 'Good bye!'


def save_and_exit():
    backup_file = r'GOIT_DZ12\backup.bin'
    with open(backup_file, 'wb') as bf:
        pickle.dump(memory, bf)
    return say_goodbye()

def show_help():
    help = '''
Список доступных команд:
"hello" - бот отвечает "How can I help you?"
"add [username] [phone] [birthday]" - бот сохраняет в памяти новый контакт. Ввведите имя и номер телефона в формате +111-222-33-44 через пробел, так же можно ввести день рождения в формате YYYY-mm-dd;
"change [username] [phone]" - бот добавляет в память новый номер телефона для существующего контакта [username].;
"phone [username]" - бот выводит все номера телефонов для указанного контакта. Вместо [username] введите имя пользователя;
"show all" - бот выводит все сохраненные контакты с их номерами телефонов в консоль в формате "Имя, телефоны: ";
"show 1" - бот выводит 1й сохраненный в памяти контакт. Чем больше число, тем больше контактов выдаст бот. Используйте это вместо show all, если хотите получить только часть адресной книги;
"goodbye", "close", "exit, stop" - бот сохраняет все данные в файл бэкапа, пишет "Good bye!" и завершает свою работу;
"clear [username]" - бот удаляет все телефоны у пользователя, чье имя идёт после слова clear. Действие необратимо и требует подтверждения;
"delete [username]" - бот удаляет из памяти все данные о пользователе, чье имя идёт после слова delete. Действие необратимо и требует подтверждения;
"del phone [username] [phone]" - бот удаляет конкретный телефон у конкретного пользователя;
"date [username]" - бот выводит день рождения пользователя [username];
"bd [username]" - бот выводит количество дней до ближайшего дня рождения пользователя [username];
"search [query]" - бот ищет совпадения со строкой [query] в адресной книге и выводит всех пользователей, чье имя или телефон совпали с запросом поиска;
'''
    return help


@input_error
def add_new_user(command: str):
    userdata = command.split()
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
    name_phone = command.split()
    name, new_phone_number = name_phone[0], name_phone[1]    
    memory.update_record(name, new_phone_number)
    message = f'Changed in memory: Name - {name}, new phone - {new_phone_number}'
    return message

@input_error
def clear_user(name: str):
    confirm = input(f'This will delete all the phones for existing user {name}. Proceed? (Y/N)\n')
    if confirm.lower() == 'y':
        memory.clear_phones(name)
        message = f'User "{name}" cleared successfully'
    else:
        message = "Action is aborted"
    return message


@input_error
def get_users_phone(name: str):
    return memory.get_phones(name)

@input_error
def get_database(num_iterations):
    if num_iterations == 'all':
        return [i for i in memory.data.values()]

    else:
        num_iterations = int(num_iterations)        
        for res in memory.iterator(num_iterations):
            return res


@input_error
def delete_user(name: str):
    confirm = input(f'This will delete the user {name}. Proceed? (Y/N)\n')
    if confirm.lower() == 'y':
        memory.remove_record(name)
        message = f'User "{name}" deleted successfully'
    else:
        message = "Action is aborted"
    return message


@input_error
def delete_phone(command: str):
    name_phone = command.split()
    name, phone_number = name_phone[0], name_phone[1]
    memory.delete_phone(name, phone_number)
    return "Phone deleted successfully"

def search(query: str):
    results = []
    for record in memory.values():
        if query in record.name.value:
            results.append(record)
            continue
        if record.search_in_phones(query):
            results.append(record)
        
    if results:
        return results
    else: 
        return 'Nothing is found'


COMMANDS_DICT = {
    'help': show_help,
    'hello': say_hello,
    'exit': save_and_exit,
    'close': save_and_exit,
    'goodbye': save_and_exit,
    'stop': save_and_exit,
    'add': add_new_user,
    'change': update_user,
    'phone': get_users_phone,
    'show': get_database,
    'clear': clear_user,
    'delete': delete_user,
    'del phone': delete_phone,
    'bd': calculate_days_to_birthday,
    'date': get_birthday,
    'search': search
}


def command_selector(command):
    return COMMANDS_DICT[command]

def parser(user_input: str):
    for key in COMMANDS_DICT:
        if user_input.lower().startswith(key):
            action = command_selector(key)
            data = user_input.removeprefix(f'{key} ')
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