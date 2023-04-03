from random import randrange


def get_numbers_ticket(min, max, quantity):
    list = []
    if min < 1 or max > 1000 or min > quantity or quantity > max:
        pass
    else:
        i = 0
        while i < quantity:
            num = randrange(min,max)
            list.append(num)
            i += 1
        list = sorted(list)
    return list