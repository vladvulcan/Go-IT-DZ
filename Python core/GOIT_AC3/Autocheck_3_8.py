def cost_delivery(*quantity,discount=0):
    goods = int(quantity[0])
    if goods == 1:
        return 5
    else:
        other_items = goods - 1
        cost = 5+2*other_items
    if not discount: return cost    
    else: return cost*discount