grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    i = 0
    list = []
    for student, grade in students.items():
            i += 1
            stroka = "{:>4}|{:<10}|{:^5}|{:^5}".format(i, student, grade, grades[grade])
            list.append(stroka)
    return list