result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        x = input()
        try:
            operand = float(x)
            if result == None:
                wait_for_number = False
                result = operand
            else:
                if operator == '+':
                    result += operand
                    wait_for_number = False
                elif operator == '-':
                    result -= operand
                    wait_for_number = False
                elif operator == '*':
                    result *= operand
                    wait_for_number = False
                else:
                    result /= operand  
                    wait_for_number = False
        except ValueError:
            print (f"{x} is not a number. Try again.")
            continue
    else:
        operator = input ()
        operators = '+-*/'
        if operator not in operators and operator != '=':
            print (f"{operator} is not '+' or '-' or '/' or '*'. Try again")
        elif operator == '=':
            print (result)
            break
        else:
            wait_for_number = True
            continue
              