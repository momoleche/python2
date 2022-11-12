print("--------------------------------")
print("1. Calcular el 30%")
print("2. Calcular el 60%")
print("1. Calcular el 90%")
opcion = int(input("Ingrese su opcion: "))
print("--------------------------------")

if opcion == 1:
    num = int(input("Ingrese un numero: "))
    total = num * 0.30

    print("El 30% de su numero es: ", total)

elif opcion == 2:
    num = int(input("Ingrese un numero: "))
    total = num * 0.60

    print("El 60% de su numero es: ", total)


elif opcion == 3:
    num = int(input("Ingrese un numero: "))
    total = num * 0.90

    print("El 90% de su numero es: ", total)

else:
    print("Ingrese un numero valido")

