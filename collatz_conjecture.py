def steps(number):

    if not number >= 1:

        raise ValueError("Only positive integers are allowed")
    
    counter = 0

    while number > 1:

        if number % 2 == 0:

            number = number // 2

            counter += 1

            print(number)

        else:

            number = number * 3 + 1

            counter += 1

            print(number)

    return counter

print(steps(12))



        
    
