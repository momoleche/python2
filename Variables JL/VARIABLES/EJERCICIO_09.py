unitario = float(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad de productos que desea llevar: "))
subtotal = unitario * cantidad

subtotal2 = subtotal * 0.16

total = subtotal + subtotal2

print("El valor que debe pagar en total con 16% de IVA es: ", total)