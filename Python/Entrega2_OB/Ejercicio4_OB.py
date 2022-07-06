num1 = int(input("Introduce el número de inicio "))
num2 = int(input("Introduce el número de fin "))

if num1 % 2 == 0:
    print("Número 1 es par ")
    for i in range(num1+1, num2+1, 2):
        print(i)
else:
    print("Número 2 es impar")
    for i in range(num1, num2+1, 2):
        print(i)
