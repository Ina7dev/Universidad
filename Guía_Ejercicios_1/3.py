from math import cos, pi, factorial

x = 0.3 * pi
cifras = 8
valor_verdadero = cos(x)  # valor verdadero de cos(0.3π)

# Criterio de Scarborough q garantiza 'cifras' cifras significativas
error_tolerado = 0.5 * 10 ** (2 - cifras)  # en porcentaje

print(f"x = {x}")
print(f"Valor verdadero cos(x): {valor_verdadero}")
print(f"Error tolerado (es): {error_tolerado} %\n")
print(f"{'Términos':>8} {'Aproximación':>18} {'Error verdadero %':>18} {'Error aprox %':>15}")

suma = 0.0
anterior = 0.0
i = 0
error_aprox = 100  # valor inicial grande para que entre al while

while error_aprox >= error_tolerado:
    termino = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    suma += termino

    error_verdadero = abs((valor_verdadero - suma) / valor_verdadero) * 100

    if i == 0:
        print(f"{i + 1:>8} {suma:>18.12f} {error_verdadero:>18.4e} {'---':>15}")
    else:
        error_aprox = abs((suma - anterior) / suma) * 100
        print(f"{i + 1:>8} {suma:>18.12f} {error_verdadero:>18.4e} {error_aprox:>15.4e}")

    anterior = suma
    i += 1

print(f"\nSe necesitaron {i} términos")
print(f"cos({x}) ≈ {suma}")