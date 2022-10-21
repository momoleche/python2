from cmath import pi


peso=float(input("Ingrese su peso : "))
altura=float(input("Ingresa tu altura: "))
operacion=peso/altura**2
print(operacion)

if operacion<20:
    print("Estas desnutrido")
elif operacion >=20 and operacion<=25:
    print("Eres normal")
elif operacion >=25 and operacion <=30:
    print("Eres un gordito uwuwwuwu")
elif operacion >=30 and operacion <=35:
    print("Obesidad grado 1")
elif operacion >=35 and operacion <=40:
    print ("Obesidad grado 2")
elif operacion >40:
    print("Obesidad grado 3")
else:
    print("esta muerto? uwuwuwuwwu")