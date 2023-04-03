def total_salary(path):
    total_salary = 0  
    f = open(path, "r")  
    try:  
        while True:  
            line = f.readline()  
            if not line:  
                break  
            values = line.split(",")  
            total_salary += float(values[1])  
        return total_salary  
    finally:  
        f.close()