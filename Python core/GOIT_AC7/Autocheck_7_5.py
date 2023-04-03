def capital_text(s):
    newS = ''
    s = s.strip()
    wait_for_upper = True
    wait_for_dot = True
    wait_for_excl = True
    wait_for_quest = True
    for letter in s:
        if letter == ' ':
            newS += letter
            continue
        if not letter.isdigit():
            if wait_for_upper:
                newS += letter.upper()
                wait_for_upper = False
                continue
            if not wait_for_dot:
                newS += letter.upper()
                wait_for_dot = True
                continue
            elif not wait_for_excl:
                newS += letter.upper()
                wait_for_excl = True
                continue
            elif not wait_for_quest:
                newS += letter.upper()
                wait_for_quest = True
                continue
            else: newS += letter
        else: newS += letter
        if letter == '.':
            wait_for_dot = False
            continue
        if letter == '!':
            wait_for_excl = False
            continue
        if letter == '?':
            wait_for_excl = False
            continue
    return (newS)