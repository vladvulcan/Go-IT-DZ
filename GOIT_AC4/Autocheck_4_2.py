def prepare_data(data):
    data.remove(max(data))
    data.remove(min(data))
    data.sort()
    return data