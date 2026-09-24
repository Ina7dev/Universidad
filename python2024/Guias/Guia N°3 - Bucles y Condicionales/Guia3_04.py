#4
n = int(input("Ingrese el número de cubos a calcular: "))

pimmpar = 1
simpares = 0
cuantosimpares = 0

for i in range(1, n + 1):
    simpares = 0
    cuantosimpares = 0
    nimpares = []
    
    while cuantosimpares < i:
        simpares += pimmpar
        nimpares.append(pimmpar)
        pimmpar += 2
        cuantosimpares += 1
    
    print(f"{i}^3 =", end=" ")
    for j in range(len(nimpares)):
        if j < len(nimpares) - 1:
            print(nimpares[j], "+", end=" ")
        else:
            print(nimpares[j], end=" ")
    
    print(f"= {simpares}")