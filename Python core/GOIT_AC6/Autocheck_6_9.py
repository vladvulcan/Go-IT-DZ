def is_equal_string(utf8_string, utf16_string):
    return True if utf8_string.decode() == utf16_string.decode('utf-16') else False