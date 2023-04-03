from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum_list = 0
    for i in number_list:
        sum_list += Decimal(i)
    return Decimal(sum_list/len(number_list))