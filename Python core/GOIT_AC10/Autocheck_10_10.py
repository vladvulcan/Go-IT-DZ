from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum (filter(lambda x:x>0,self))