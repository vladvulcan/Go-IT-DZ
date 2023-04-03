from functools import reduce


def amount_payment(payment):
    return reduce(lambda x,y: (x if x>0 else 0)+(y if y>0 else 0),payment)