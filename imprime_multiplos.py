def imprimeMultiplos(n):

    i = 1

    while i <= 6:

        print(f"{n*i} \t")

        i = i + 1

    return i

def imprime_tabla(n):

    i = 1 

    while i <= 6:

        imprimeMultiplos(n)

        i += 1

    return i


print(imprime_tabla(12))