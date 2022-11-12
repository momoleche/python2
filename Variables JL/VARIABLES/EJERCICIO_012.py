import math

#Le pedimos al usuario los 2 catetos
cateto1 = float(input("Introducir el Primer cateto: "))
cateto2 = float(input("Introducir el Segundo cateto: "))


hipotenusa = math.sqrt((cateto1**2) + (cateto2**2)**(1/2))

print("Hipotenusa: ", hipotenusa)