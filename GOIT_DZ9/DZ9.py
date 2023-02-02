memory = {}
name = ''
phone_number = ''

def input_error(func):
    def inner(command):
        try:
            res = func(command)
            return res

        except KeyError:
            print ('Enter user name')
        
        except ValueError:
            print ('Error')

        except IndexError:
            print ('Error')

    return inner

@input_error
def main(command = input()):
    while True:
        command = command.lower()

        if command == '.':
            break

        elif command == 'hello':
            print ('How can I help you?')

        elif command == f'add {name}{phone_number}':
            memory[name] = phone_number
        
        elif command == f'change {name}{phone_number}':
            if name in memory:
                memory[name] = phone_number
            else:
                print ("no such name")
        
        elif command == f'phone {name}':
            print (memory.get(name,"Error"))

        elif command == "show all":
            for key, value in memory.items():
                print (f'{key}:{value}')

        elif command in ['goodbye', 'close', 'exit']:
            print ("Good bye!")
            break

        else:
            continue


    
