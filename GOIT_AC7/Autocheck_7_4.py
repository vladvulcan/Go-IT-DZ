def is_integer(s):
    s = s.strip()
    s = s.removeprefix('+')
    s = s.removeprefix('-')
    if len(s) == 0:
        return False
    if s.isdigit():
        return True
    else: return False