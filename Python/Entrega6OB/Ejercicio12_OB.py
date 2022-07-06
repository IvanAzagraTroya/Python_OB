class Vehiculo():
    marca = ""
    matricula = ""

    def __init__(self, marca, matricula):
        self.marca = marca
        self.matricula = matricula

    def __str__(self):
        return f"Marca: {self.marca}, matricula: {self.matricula}"


vehiculo = Vehiculo(marca=input(
    "Introduce la marca: "), matricula=input("Introduce la matricula: "))

print("")

# Escritura
f = open("concesionario.txt", "at")
f.write(str(vehiculo)+'\n')
f.close()

# Lectura
f1 = open('concesionario.txt', 'r')
datos = f1.read()
f1.close()

print(datos)
