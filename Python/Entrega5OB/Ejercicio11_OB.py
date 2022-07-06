from datetime import datetime

now = datetime.now()

print("Es la:", now.hour)

if now.hour > 19:
    print("Has terminado la jornada, a descansar")
else:
    restante = 19 - now.hour
    print("Quedan:", restante, "horas restantes")
