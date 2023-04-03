def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    try:
        for i in employee_list:
            file.write(i)
            for j in i:
                file.write(j+'\n')
    finally:
        file.close()