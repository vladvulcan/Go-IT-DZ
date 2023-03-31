def lookup_key(data, value):
    a = []
    for key, val in data.items():
        if val == value:
            a.append(key)
    return a