import math

def tables():

    x = 1.0

    while x < 2**16:

        try:
            valor = math.exp2(x)    
            print(f"{x:>6.0f}\t{valor:>20.11f}") 

        except OverflowError:
            print(f"{x:>6.0f}\t{'inf':>20}")
            
        x += 1

tables()

