memory = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res

        except KeyError:
            return "No such name"
        
        except ValueError as err:
            return err

        except IndexError:
            return 'Name is given, but phone number is not'
        
        except TypeError:
            return "Give me name and phone please"

    return inner

@input_error
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
    name, phone_number = name_phone[0], name_phone[1]
    if not name.isalpha():
        raise ValueError('Name must be a text, not number')
    if not phone_number.isdecimal():
        raise ValueError('Numbers-only phones are allowed')
    if name in memory:
        raise ValueError(f'This name already exists.\nType "phone {name}" to see the number linked to it.')
    else: memory[name] = phone_number
    message = f'Added to memory: Name - {name}, phone - {phone_number}'
    return message
    
@input_error
def change_existing_users_phone(command: str):
    name_phone = command[1:].split()
    name, new_phone_number = name_phone[0], name_phone[1]
    if not new_phone_number.isdecimal():
        raise ValueError('Numbers-only phones are allowed')    
    if not name in memory:
        raise KeyError
    memory[name] = new_phone_number
    message = f'Changed in memory: Name - {name}, new phone - {new_phone_number}'
    return message

@input_error
def get_users_phone(command: str):
    name = command[1:]
    return memory[name]

@input_error
def get_database():
    contacts = ''
    for key, value in memory.items():
         contacts += f'{key} : {value} \n'
    return contacts



COMMANDS_DICT = {
    'help': show_help,
    'hello': say_hello,
    'exit': say_goodbye,
    'close': say_goodbye,
    'good bye': say_goodbye,
    'add': add_new_user,
    'change': change_existing_users_phone,
    'phone': get_users_phone,
    'show all': get_database
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
    
