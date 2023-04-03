def discount_price(discount):
    def inner(price):
        return price*(1-discount)
    return inner