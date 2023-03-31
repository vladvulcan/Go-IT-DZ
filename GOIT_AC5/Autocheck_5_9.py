def formatted_numbers():
    list = ['| decimal  |   hex    |  binary  |',]
    for num in range(16):
        s = "|{:<10d}|{:^10x}|{:>10b}|".format(num, num, num)
        list.append(s)
    return list