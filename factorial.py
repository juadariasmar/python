def factorial(n):
    if type(n) != type(1):
        print('El factorial solo es para numeros enteros')
        return 1
    elif n < 0:
        print('el factorial solo es para numeros enteros')
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(-1))
