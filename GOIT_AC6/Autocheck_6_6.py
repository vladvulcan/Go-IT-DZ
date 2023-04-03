def get_recipe(path, search_id):
    search = None
    dict = {}
    with open (path,"r") as file:
        while True:
            line = file.readline()
            if search_id in line:
                recipe = line.split(',')
                dict["id"] = recipe[0]
                dict["name"] = recipe[1]
                if '\n' in recipe[-1]:
                    last =recipe[-1][:-1]
                    ingr = [recipe[2],recipe[3],last]
                else:
                    ingr = [recipe[2],recipe[3],recipe[4]]
                dict["ingredients"] = ingr
                search = dict
            if not line:
                break
    return search