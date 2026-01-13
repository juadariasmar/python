def pendiente(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def intercepta(x1, y1, x2, y2):
    return y1 - pendiente(x1, y1, x2, y2) * x1


print(intercepta(1,3, 2, 6))


