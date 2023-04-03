def make_request(keys, values):
    dict = {}
    if len(keys) == len(values):
        for i, j in zip (keys, values):
            dict[i] = j
    return dict