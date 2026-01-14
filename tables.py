import math

def tables():

    x = 1.0

    while x < 10.0:
        print(f"{x:>2.0f}\t{math.log(x):>20.11f}") 
        x += 1

tables()

