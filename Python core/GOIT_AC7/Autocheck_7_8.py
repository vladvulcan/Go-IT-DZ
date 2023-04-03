def token_parser(s):
    list = []
    if len (s) ==0:
        pass
    else:
        stroka = ''
        for i in s:
            if not i == ' ':
                if i in '*/-+()':
                    if len(stroka) != 0: 
                        list.append(stroka)
                        stroka = ''
                        list.append(i)
                    else: list.append(i)
                    
                else: stroka+=i
        list.append(stroka)   
    return list