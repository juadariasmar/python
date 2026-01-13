import math

def area(radio):
    return math.pi * radio**2

def dist(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dalcuadrado = dx**2 + dy**2
    result = math.sqrt(dalcuadrado)
    return result

def area2(xc, yc, xp, yp): 
    return area(dist(xc, yc, xp, yp))


area2(2, 4, 3, 5)





