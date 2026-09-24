booleano = 42 == 42
print(booleano)


#NEGAR UN BOOLEANO.
b = not False
print(b)


bo = True and True
print(bo)

#Utilizando and
v = 42 > 32 and 32 < 42
print(f"es {v}")

#Utilizando or
va = 23 > 42 or 23 < 42
print(f"es {va}")

#OPERADORES LOGICOS.
a=10
b=15
c=20
resultado = ((a<b) and (b<c))
r2 = ((a>b) and (b<c))
r3 = ((a>b) or (b<c))
r4 = not ((a>b) or (b<c))
print(resultado)
print(r2)
print(r3)
print(r4)