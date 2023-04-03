def format_phone_number(func):
    def inner(phone):
        sanitized_number = func(phone)
        if len(sanitized_number) == 12:
            return f'+{func(phone)}'
        elif len(sanitized_number) == 10:
            return f'+38{func(phone)}'
        else: return func(phone)
    return inner
        
@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone