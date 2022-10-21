valor=float(input("ingrese el monto de la cuenta: "))
if valor <=150000:
    print("PAGA EN EFECTIVO")
elif valor >=150000 and valor<=300000:
    print("PAGA CON CELULAR")
elif valor >=300000 and valor<=600000:
    print("PAGA CON TARJETA DEBITO")
else:
    print("PAGA CON TARJETA DE CREDITO")
