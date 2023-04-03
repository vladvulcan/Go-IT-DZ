class IDException(Exception):
    pass


def add_id(id_list:list, employee_id: str):
    if employee_id.startswith('01'):
        id_list.append(employee_id)
        return id_list
    else: raise IDException