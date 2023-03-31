def game(terra, power):
    for i in terra:
        for j in i:
            if j <= power:
                power += j
            else: break
    return power