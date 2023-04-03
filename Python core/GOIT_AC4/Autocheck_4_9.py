def is_valid_pin_codes(pin_codes):
    check = None
    if len (pin_codes) != 0:
        for i in pin_codes:
            try:
                if pin_codes.count(i) > 1 or type(i) is not str or len(i) != 4:
                    return False
                else:
                    i = int(i)
                    check = True
                    continue
               
            except ValueError: return False
        return check
    else: return False