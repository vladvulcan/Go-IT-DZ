import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    out = []
    for cat in cats:
        if isinstance(cats[0],Cat):        
             out.append({"nickname":cat.nickname,"age":cat.age,"owner":cat.owner})

        elif isinstance(cats[0],dict):
            list = [i for i in cat.values()]
            out.append(Cat(list[0],list[1],list[2]))
            
    return out