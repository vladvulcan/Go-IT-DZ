def sanitize_phone_number(phone):
    number =''
    for i in phone.strip():
        if i not in [ '(', ')', '-', '+', ' ']:
            number += i
    return number