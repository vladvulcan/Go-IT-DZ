memory = {}
name = ''
phone_number = ''

def input_error(func):
    def inner(command):
        try:
            res = func(command)
            return res

        except KeyError:
            return ("No such name")        
        
        except ValueError as msg:
            return (msg)

        except IndexError:
            return ('Name is given, but phone number is not')

    print (inner)


def main():
    while True:
        command = input('enter command: ')
        command = command.lower()

        if command == '.':
            break

        elif command == 'hello':
            print ('How can I help you?')

        elif command.startswith('add'):            
            add_command = command.removeprefix('add')
            if len(add_command)>0:
                add(add_command)
            else:
                print ("Give me name and phone please")
            
        
        elif command.startswith('change'):
            change_command = command.removeprefix('change')
            if len(change_command)>0:
                change(change_command)
            else:
                print ("Give me name and phone please")
            
        
        elif command.startswith('phone'):
            name = command.removeprefix('phone')
            if len(name)>0:
                print (memory.get(name,"No such name"))
            else:
                print("Enter user name")

        elif command == "show all":
            for key, value in memory.items():
                print (f'{key}: {value}')

        elif command in ['goodbye', 'close', 'exit']:
            print ("Good bye!")
            break

        elif command == 'help':
            help = '''
Список доступных команд:
"hello" - бот отвечает "How can I help you?"
"add ..." -   бот сохраняет в памяти новый контакт. Вместо ... введите имя и номер телефона через пробел.
"change ..." - бот сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... введите имя и номер телефона.
"phone ..." - бот выводит в консоль номер телефона для указанного контакта. Вместо ... введите имя пользователя через пробел.
"show all" - бот выводит все сохраненные контакты с номерами телефонов в консоль в формате "Имя: телефон".
"good bye", "close", "exit" - бот пишет "Good bye!" и завершает свою работу.
            '''
            print (help)

        else:
            print(
            '''Invalid command. Try again.
For the list of available commands type "help"''')
            continue

@input_error
def add(command: str):    
    global memory
    name_phone = command.split()
    name, phone_number = name_phone[0], name_phone[1]
    if not isinstance(name,str):
        raise ValueError('Name must be a string')
    if not isinstance(phone_number,int):
        raise ValueError('Number must be int')
    memory[name] = phone_number
    print (f'Added to memory: Name - {name}, phone - {phone_number}')
    
@input_error
def change(command: str):
    global memory
    name_phone = command.split()
    name, new_phone_number = name_phone[0], name_phone[1]    
    old_number = memory[name]
    memory[name] = new_phone_number
    print (f'Changed in memory: Name - {name}, new phone - {new_phone_number}')
  


if __name__ == '__main__':
    main()
    
