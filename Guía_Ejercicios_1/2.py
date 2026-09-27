from math import factorial

x = 5
n = 20
valor_verdadero = 6.737947e-3  # valor verdadero de e^-5 que da el enunciado

# e^-x = 1 - x + x^2/2 - x^3/3! + ...
print("MÉTODO 1: e^-x = 1 - x + x^2/2! - x^3/3! + ...")
print(f"{'Términos':>8} {'Aproximación':>15} {'Error verdadero %':>18} {'Error aprox %':>15}")

suma_m1 = 0.0
anterior_m1 = 0.0

for i in range(n):
    termino = ((-1) ** i) * (x ** i) / factorial(i)
    suma_m1 += termino

    error_verdadero = abs((valor_verdadero - suma_m1) / valor_verdadero) * 100

    if i == 0:
        print(f"{i + 1:>8} {suma_m1:>15.6e} {error_verdadero:>18.4e} {'---':>15}")
    else:
        error_aprox = abs((suma_m1 - anterior_m1) / suma_m1) * 100
        print(f"{i + 1:>8} {suma_m1:>15.6e} {error_verdadero:>18.4e} {error_aprox:>15.4e}")

    anterior_m1 = suma_m1


# e^-x = 1 / (1 + x + x^2/2 + ...)
print("\nMÉTODO 2: e^-x = 1 / (1 + x + x^2/2! + x^3/3! + ...)")
print(f"{'Términos':>8} {'Aproximación':>15} {'Error verdadero %':>18} {'Error aprox %':>15}")

suma_m2 = 0.0      # aquí se va sumando e^x
anterior_m2 = 0.0  # aproximación anterior de e^-x

for i in range(n):
    termino = (x ** i) / factorial(i)
    suma_m2 += termino
    aprox_m2 = 1 / suma_m2  # e^-x = 1 / e^x

    error_verdadero = abs((valor_verdadero - aprox_m2) / valor_verdadero) * 100

    if i == 0:
        print(f"{i + 1:>8} {aprox_m2:>15.6e} {error_verdadero:>18.4e} {'---':>15}")
    else:
        error_aprox = abs((aprox_m2 - anterior_m2) / aprox_m2) * 100
        print(f"{i + 1:>8} {aprox_m2:>15.6e} {error_verdadero:>18.4e} {error_aprox:>15.4e}")

    anterior_m2 = aprox_m2