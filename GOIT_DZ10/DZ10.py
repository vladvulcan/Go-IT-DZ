from collections import UserDict   


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
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone): 
       self.phones.append(Phone(phone).value)

    def clear_phones(self): 
        self.phones.clear()

        

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def update_record(self,name,phone):
       self.data[name].add_phone(phone)

    def get_phones(self,name):
        return self.data[name].phones
    
    def remove_record(self, name):
        del self.data[name]
    
    def clear_phones(self, name):
        self.data[name].clear_phones()

   

    
    
    
 
memory = AddressBook()          


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
    name_phone = command[1:].split()
    if not name_phone[0].isalpha():
        raise ValueError('Name must be a text, not number')
    if not name_phone[1].isdecimal():
        raise ValueError('Numbers-only phones are allowed')
    new_user = Record(name_phone[0])
    if new_user.name.value in memory:
        raise ValueError(f'This name already exists.\nType "phone {name_phone[0]}" to see the number linked to it.')    
    else:        
        new_user.add_phone(name_phone[1])    
        memory.add_record(new_user)
    message = f'Added to memory: Name - {name_phone[0]}, phone - {name_phone[1]}'
    return message
    
@input_error
def update_user(command: str):
    name_phone = command[1:].split()
    name, new_phone_number = name_phone[0], name_phone[1]
    if not new_phone_number.isdecimal():
        raise ValueError('Numbers-only phones are allowed')
    memory.update_record(name, new_phone_number)
    message = f'Changed in memory: Name - {name}, new phone - {new_phone_number}'
    return message

@input_error
def delete_user(command: str):
    name = command[1:]
    confirm = input(f'This will delete the user {name}. Proceed? (Y/N)\n')
    if confirm == 'Y':
        memory.clear_phones(name)
    return f'User "{name}" deleted successfully'


@input_error
def get_users_phone(command: str):
    name = command[1:]
    return memory.get_phones(name)

@input_error
def get_database():
    contacts = ''
    for key, value in memory.data.items():
         contacts += f'{key} : {value.phones} \n'
    return contacts

@input_error
def delete_all_phones(command: str):
    name = command[1:]
    confirm = input(f'This will delete all the phones for existing user {name}. Proceed? (Y/N)\n')
    if confirm == 'Y':
        memory.remove_record(name)
    return f'User "{name}" cleared successfully'



COMMANDS_DICT = {
    'help': show_help,
    'hello': say_hello,
    'exit': say_goodbye,
    'close': say_goodbye,
    'good bye': say_goodbye,
    'add': add_new_user,
    'change': update_user,
    'phone': get_users_phone,
    'show all': get_database,
    'clear': delete_all_phones,
    'delete': delete_user
    
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
    
