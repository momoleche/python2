nota1=int(input("digite su primer nota: "))
nota2=int(input("digite su segunda nota: "))
nota3=int(input("digite su tercera nota: "))
nota4=int(input("digite su cuarta nota: "))
nota5=int(input("digite su quinta nota: "))
suma=nota1+nota2+nota3+nota4+nota5
division=suma/5

if division <=29:
    print("REPROBADO SU NOTA ES DE ", division)
elif division >=30:
    print("APROBADO SU NOTA ES DE ", division)