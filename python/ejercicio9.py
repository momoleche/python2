tamaño=int(input("QUE TAMAÑO ES LA PIZA :"))
ingredientes=input("Cuantos ingredientes adicionales:")
 
if tamaño==1: 
    costo_tamaño= 15000 
if tamaño==2:
    costo_tamaño= 24000
if tamaño==3:
    costo_tamaño = 36000

costo_ingredientes = 4000
total= costo_tamaño +costo_ingredientes 
 
print("el costo es de " ,total," pesos")