def get_cats_info(path):
    with open (path,'r') as file:
        list = []
        while True:
            dict = {}
            line = file.readline().split(',')
            # return line
            try:
                dict["id"]=line[0]
                dict["name"]=line[1]
                if '\n' in line[2]:
                    dict["age"]=line[2][:-1]
                else:
                    dict["age"]=line[2]
                list.append(dict)
            except IndexError: break
            if not line:
                break
    return list