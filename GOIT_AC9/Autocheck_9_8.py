def get_emails(list_contacts):
    return [i for i in map(lambda user: user.get('email'),list_contacts)]