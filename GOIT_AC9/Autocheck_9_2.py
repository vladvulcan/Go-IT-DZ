DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    discount = customer.get('discount',DEFAULT_DISCOUNT)
    return price * (1 - discount)