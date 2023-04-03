def generator_numbers(string=""):
    number = ''
    for symbol in string:        
        if symbol.isdigit():
            number += symbol
        else:
            if len(number) != 0:
                yield int(number)
                number = ''
        

def sum_profit(string):
    return sum([i for i in generator_numbers(string)])