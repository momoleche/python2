cantidad=int(input("Cantidad: "))

if cantidad<5:
    precio=float(input("Precio unitario: "))
    print("No aplica descuento total: ",precio*cantidad)
elif cantidad >5 and cantidad <10:
    precio=float(input("Precio unitario: "))
    descuento=5/100
    descuento2=precio*descuento
    total=precio-descuento2
    print("Aplica un descuento del 5%", total*cantidad)
elif cantidad >10 :
    precio=float(input("Precio unitario: "))
    descuento=8/100
    descuento2=precio*descuento
    total=precio-descuento2
    print("Aplica un descuento del 8%",100/descuento)
else:
    print("?")