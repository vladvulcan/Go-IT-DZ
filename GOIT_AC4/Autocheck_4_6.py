def split_list(grade):
    les = []
    high = []
    for i in grade:
        avg = sum(grade)/len(grade)
        if i <= avg:
            les.append(i)
        else:
            high.append(i)
    return les, high