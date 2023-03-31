def is_valid_password(password):
    is_8_symbols = None
    is_uppercase = None
    is_lowercase = None
    is_number = None
    isvalid = False
    if len(password) == 8:
         is_8_symbols = True 
    else: return False
    for i in password:
        if is_uppercase == True and is_lowercase == True and is_number == True:
            isvalid = True
            return isvalid
        else:
            if is_uppercase != True:
                if ord(i) in range (65, 91):
                    is_uppercase = True
                    continue
            if is_lowercase != True:
                if ord(i) in range (97, 123):
                    is_lowercase = True
                    continue
            if is_number != True:
                if ord(i) in range (48, 58):
                    is_number = True
                    continue
            else: continue
    if is_uppercase == True and is_lowercase == True and is_number == True:
            isvalid = True    
    return isvalid