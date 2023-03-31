def format_ingredients(items):
    ingredients = ''
    for i in items:
        if i == items[0]:
            ingredients += f"{i}"
        elif i == items[-1]:
            ingredients += f" and {i}"
        else:
            ingredients += f", {i}"
    return ingredients