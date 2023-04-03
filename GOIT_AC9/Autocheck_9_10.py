def get_favorites(contacts):
    return [i for i in filter(lambda user: user.get('favorite') == True,contacts)]