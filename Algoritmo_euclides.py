# programa que calcula el mcd con el algoritmo de euclides y despues el mcm

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 <= 0 or num2 <= 0:
    print("Los dos números tienen que ser enteros positivos.")
else:
    # dejamos el mayor como dividendo y el menor como divisor
    dividendo = max(num1, num2)
    divisor = min(num1, num2)

    print(f"\n{'Dividendo':>10} {'Divisor':>8} {'Cociente':>9} {'Resto':>6}")

    # euclides: se divide, y mientras el resto no sea 0
    # el divisor pasa a ser el dividendo y el resto pasa a ser el divisor
    while divisor != 0:
        cociente = dividendo // divisor
        resto = dividendo % divisor
        print(f"{dividendo:>10} {divisor:>8} {cociente:>9} {resto:>6}")

        dividendo = divisor
        divisor = resto

    mcd = dividendo  # el ultimo divisor que dio resto 0

    # el mcm se saca con la relacion: mcd * mcm = num1 * num2
    mcm = (num1 * num2) // mcd

    print(f"\nEl máximo común divisor de {num1} y {num2} es {mcd}")
    print(f"El mínimo común múltiplo de {num1} y {num2} es {mcm}")