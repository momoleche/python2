print("----MENU-----")
print("1. CUADRADO  ")
print("2. RECTANGULO")
print("3. TRIANGULO ")
print("4. CIRCULO   ")
print("5. ROMBO     ")
print("6. TRAPECIO  ")

opcion = int(input("INGRESE LA OPCION DESEADA "))

if opcion == 1:
    numero1=int(input("Digite el largo del cuadrado: "))
    numero2=int(input("Digite el ancho del cuadrado: "))
    print(numero1*numero2)
elif opcion==2:
    numero1=int(input("Digite la base del rectangulo: "))
    numero2=int(input("Digite la altura del rectangulo: "))
    print(numero1*numero2)
elif opcion==3:
    numero1=int(input("Digite la base del triangulo: "))
    numero2=int(input("Digite la altura del triangulo: "))
    print(numero1*numero2/2)
elif opcion==4:
    numero1=int(input("Digite el perimetro del circulo: "))
    numero2=int(input("Digite el radio del circulo  "))
    print(numero1*numero2/2)
elif opcion==5:
    numero1=int(input("Digite la diagonal mayor"))
    numero2=int(input("Digite la diagonal menor  "))
    print(numero2*numero1/2)
elif opcion==6:
    numero1=int(input("Digite la base menor: "))
    numero2=int(input("Digite la base mayor  "))
    numero3=int(input("Digite la altura  "))
    operacion=(numero1+numero2)
    print(operacion/2*numero3)
else:
    print("opcion incorreta")





