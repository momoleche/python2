diario = float(input("Ingrese su salario diario: "))
dias = int(input("Ingrese el numero de dias trabajados: "))
pago = diario * dias

pension = pago * 0.10
salud = pago * 0.15


total = pago - (pension + salud) 

print(pago)
print(pension)
print(salud)
print(total)
print("El pago que recibe el empleado es ", total, " teniendo en cuenta que se descuenta el 10% de la pension ", pension," y el 15% de salud ",salud)
