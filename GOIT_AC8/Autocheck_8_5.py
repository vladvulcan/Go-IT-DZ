import random


def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []
    else:
        IDs = participants.keys()
        IDs = list(IDs)
        random.shuffle(IDs)
        winners = random.sample(IDs,k=2)
        return winners