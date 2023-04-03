def save_applicant_data(source, output):
    with open (output, "w") as file:
        for student in source:
            list = [val for val in student.values()]
            file.write(','.join(str(i) for i in list) + '\n')