año = int(input("Introduce el número del año: "))


def compruebaBisiesto(año):
    if año % 4 == 0:
        return "Es bisiesto"
    else:
        return "No es bisiesto"


print(compruebaBisiesto(año))
