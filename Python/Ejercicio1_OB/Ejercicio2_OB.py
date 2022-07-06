print("Introduzca su altura en metros y su peso en kilogramos")
altura = float(input("Introduzca la altura: "))
peso = float(input("Introduzca el peso: "))
print(f"La altura introducida es: {altura} metros y el peso: {peso} kg")

imc = round(peso/altura**2, 2)
print(f"El indice de masa corporal es: {imc}")
