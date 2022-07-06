import math

altura = float(input("Introduce la altura: "))
base = float(input("Introduce base: "))


def calculaArea(altura, base):
    return base * altura


print(calculaArea(altura, base))

radio = float(input("Introduce el radio: "))


def calculaAreaCirculo(radio):
    return (radio * radio) * math.pi


print(calculaAreaCirculo(radio))
