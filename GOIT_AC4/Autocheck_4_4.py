def get_grade(key):
    if key == 'F':
        x = 1 
    elif key == 'FX':
        x = 2
    elif key == 'E' or key == 'D':
        x = 3
    elif key == 'C':
        x = 4
    elif key == 'B' or key == 'A':
        x = 5
    else:
        x = None
    return x


def get_description(key):
    if key == 'F' or key == 'FX':
        x = 'Unsatisfactorily' 
    elif key == 'E':
        x = 'Enough'
    elif key == 'D':
        x = 'Satisfactorily'
    elif key == 'C':
        x = 'Good'
    elif key == 'B':
        x = 'Very good'
    elif key == 'A':
        x = 'Perfectly'
    else:
        x = None
    return x