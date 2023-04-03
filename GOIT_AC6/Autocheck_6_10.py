def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for login, password in users_info.items():
            file.write((login+':'+password+'\n').encode())