def get_employees_by_profession(path, profession):
   with open (path,'r') as file:
        text = file.readlines()
        search_res = []
        for line in text:
            prof_line = line.find(profession)
            if prof_line != -1:
                search_res.append(line)
        for res in search_res:
            ind = search_res.index(res)
            res2 = res.replace('\n','')
            res2 = res2.replace(' ','')
            res2 = res2.replace(profession,'')
            search_res[ind] = res2
        return ' '.join(search_res)