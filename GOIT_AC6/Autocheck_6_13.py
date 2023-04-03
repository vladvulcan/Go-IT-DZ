import shutil
def create_backup(path, file_name, employee_residence):
    with open(f'{path}/{file_name}', 'wb') as f:
        for key, value in employee_residence.items():  
            f.write((f'{key} {value}\n').encode()) 
        archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name