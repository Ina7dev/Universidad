from math import cos, pi, factorial

x = 0.3 * pi
cifras = 8
valor_verdadero = cos(x)

# error tolerado para 8 cifras significativas, en porcentaje
error_tolerado = 0.5 * 10 ** (2 - cifras)

print(f"Valor verdadero: {valor_verdadero}")
print(f"Error tolerado: {error_tolerado}")

suma = 0.0
anterior = 0.0
i = 0
error_aprox = 100  # parte en 100 para que entre al while

while error_aprox >= error_tolerado:
    termino = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    suma += termino

    error_verdadero = abs((valor_verdadero - suma) / valor_verdadero) * 100

    if i == 0:
        print(f"Termino {i + 1}: {suma}  Error verdadero: {error_verdadero}")
    else:
        error_aprox = abs((suma - anterior) / suma) * 100
        print(f"Termino {i + 1}: {suma}  Error verdadero: {error_verdadero}  Error aproximado: {error_aprox}")

    anterior = suma
    i += 1

print(f"Se necesitaron {i} terminos")
print(f"Resultado: {suma}")