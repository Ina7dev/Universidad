from math import factorial

x = 5
n = 20
valor_verdadero = 6.737947e-3  # valor que da el enunciado

# metodo 1, la serie con signos alternados
suma_m1 = 0.0
anterior = 0.0

print("Metodo 1")
for i in range(n):
    termino = ((-1) ** i) * (x ** i) / factorial(i)
    suma_m1 += termino

    error_verdadero = abs((valor_verdadero - suma_m1) / valor_verdadero) * 100

    if i == 0:
        # en el primer termino no hay valor anterior para comparar
        print(f"Termino {i + 1}: {suma_m1}  Error verdadero: {error_verdadero}")
    else:
        error_aprox = abs((suma_m1 - anterior) / suma_m1) * 100
        print(f"Termino {i + 1}: {suma_m1}  Error verdadero: {error_verdadero}  Error aproximado: {error_aprox}")

    anterior = suma_m1


# metodo 2, se calcula e^x y despues se hace 1 dividido en eso
suma_m2 = 0.0
anterior = 0.0

print("\nMetodo 2")
for i in range(n):
    termino = (x ** i) / factorial(i)
    suma_m2 += termino
    resultado = 1 / suma_m2

    error_verdadero = abs((valor_verdadero - resultado) / valor_verdadero) * 100

    if i == 0:
        print(f"Termino {i + 1}: {resultado}  Error verdadero: {error_verdadero}")
    else:
        error_aprox = abs((resultado - anterior) / resultado) * 100
        print(f"Termino {i + 1}: {resultado}  Error verdadero: {error_verdadero}  Error aproximado: {error_aprox}")

    anterior = resultado