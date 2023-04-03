def normal_name(list_name: list):   
    return [new_name for new_name in map(lambda name: f'{name[0].upper()}{name[1:]}', list_name)]