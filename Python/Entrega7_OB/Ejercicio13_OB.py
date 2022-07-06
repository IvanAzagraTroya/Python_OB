paises = input("Introduce paises separados por coma: ")

listaPaises = [pais for pais in paises.split(",")]
print(",".join(sorted(list(set(listaPaises)))))
