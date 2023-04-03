def get_credentials_users(path):
    with open(path, 'rb') as file:
        list = file.readlines()
        for i in range(len(list)):
            list[i] = list[i].decode().removesuffix('\n')
        return list