points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0
    l = len(coordinates)
    if l <2:
        return 0
    for i in range(1,l):
        p1 = coordinates[i-1]
        p2 = coordinates[i]
        if p1 < p2:
            R = points[p1, p2]
        elif p1 > p2:
            R = points[p2, p1]
        else: R = 0
        distance += R
    return distance