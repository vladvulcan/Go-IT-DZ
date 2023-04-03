def add_employee_to_file(record, path):
    file = open(path, 'a')
    try:
        file.write(record+'\n')
    finally:
        file.close()