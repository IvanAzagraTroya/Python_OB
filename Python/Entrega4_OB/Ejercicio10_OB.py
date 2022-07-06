class Alumno:
    nombre = ""
    nota = 0

    def introduceNombre(self, alumno):
        self.nombre = alumno

    def introduceNota(self, nota):
        self.nota = nota

    def estado(self):
        if self.nota > 5:
            return "Aprobado"
        else:
            return "Suspenso"


alumno = Alumno()
alumno.introduceNombre("Ivan")
alumno.introduceNota(10)

print(alumno.nombre)
print(alumno.nota)
print(alumno.estado())
