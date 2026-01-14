def num_par(num):

    if num < 2:
        return f"{num} debe ser mayor a 2 para poder calcular si es par o no"
    
    while num > 2:

        if num % 2 == 0:

            return f"{num} es par"
        else:
            return f"{num} no es par"
        
print(num_par(1))