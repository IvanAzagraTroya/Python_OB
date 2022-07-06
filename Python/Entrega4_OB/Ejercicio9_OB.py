class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0.0

    def __init__(self, velocidad, cilindrada,  color, ruedas, puertas):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.ruedas = ruedas
        self.puertas = puertas
        self.color = color


coche = Coche(180, 2.3, "Verde", 4, 5)
print("cilindrada: ", coche.cilindrada)
print("velocidad: ", coche.velocidad)
print("color: ", coche.color)
print("Número de puertas: ", coche.puertas)
print("Número de ruedas: ", coche.ruedas)
