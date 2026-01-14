def nLineas(n):

    if n > 0:

        print()
        nLineas(n-1)

n = int(input("Ingresa el número de saltos de línea: "))
nLineas(n)

