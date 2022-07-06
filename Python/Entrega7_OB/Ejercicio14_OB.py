from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def suma(a, b):
    return a+b


def esImpar(num):
    if num % 2 != 0:
        return True
    return False


impares = filter(esImpar, lista)
lista2 = list(impares)
print("Lista de impares: ", lista2)
resultado = reduce(suma, lista2)

print(resultado)
