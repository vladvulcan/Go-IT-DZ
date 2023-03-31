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


def get_phone_numbers_for_countries(list_phones):
    UA_numbers = []
    JP_numbers = []
    TW_numbers = []
    SG_numbers = []
    for i in list_phones:
        x = sanitize_phone_number(i)
        if x.startswith('81'):
            JP_numbers.append(x)
        elif x.startswith('65'):
            SG_numbers.append(x)
        elif x.startswith('886'):
            TW_numbers.append(x)
        else: UA_numbers.append(x)

    phones_by_country = {'JP': JP_numbers, 'SG': SG_numbers, 'TW': TW_numbers, 'UA': UA_numbers}

    return phones_by_country