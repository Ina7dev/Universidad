num = int(input("Ingresa un numero: "))

if num <= 1:
    print("No es primo")
else:
    for i in range(2, num): 
        if num % i == 0:
            print("No es primo")
            break
    else: 
        print("Es primo")