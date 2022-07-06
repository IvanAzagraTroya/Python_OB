num = int(input("Introduce un número: "))


def comprobacion(num):
    if num % 2 == 0:
        return "Es primo"
    else:
        return "No es primo"


print(comprobacion(num))
