exponentes_primos_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                         41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primos_mersene = []

for p in exponentes_primos_100:
    num = (2 ** p) - 1
    limite = int(num ** 0.5) + 1
    
    for i in range(2, limite):
        if num % i == 0:
            print(f"p={p}, no es primo")
            break
    else:
        primos_mersene.append(num)
        print(f"p={p}, es primo")