def read_employees_from_file(path):
    fh = open(path,'r')
    list = []
    try:
        i = 0
        while i <3:
            line = fh.readline()
            if '\n' in line:
                list.append(line[:-1])
            else: list.append(line)
            i += 1
            # if not line:
            #     break
    finally:
        fh.close()
        return list