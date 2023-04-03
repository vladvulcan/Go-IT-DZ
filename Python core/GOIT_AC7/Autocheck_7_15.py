def flatten(data):  
    if not data:  
        return []  
    if type(data[0]) is list:  
        return flatten(data[0]) + flatten(data[1:])  
    else:  
        return [data[0]] + flatten(data[1:])