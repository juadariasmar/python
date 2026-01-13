def estaEntre(x,y,z):

    if y <= x <= z:
        return 1
    else:
        return 0

print(estaEntre(3, 4, 8))
