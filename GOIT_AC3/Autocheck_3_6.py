def format_string(string, length):
    if len (string) >= length:
        return string
    else:
        n_spaces = (length - len(string)) // 2
        space = ' '
        return space*n_spaces+string