def sqr(x):

    if x < 2:
        return x
    
    last_guess = x/2

    while True: 

        guess = (last_guess + (x/last_guess))/2

        if abs(guess - last_guess) < 1e-7:

            return int(guess)
        
        last_guess = guess


print(sqr(8))