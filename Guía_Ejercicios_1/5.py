valor_verdadero = 0.69314718056  # ln(2) que da el enunciado

# a) y b) sumas parciales de s4 a s8 con sus errores
suma = 0.0
for n in range(1, 9):
    termino = ((-1) ** (n + 1)) / n
    suma += termino

    if n >= 4:  # solo se piden desde s4
        error_absoluto = abs(valor_verdadero - suma)
        error_relativo = error_absoluto / valor_verdadero * 100
        print(f"S{n} = {suma}  Error absoluto: {error_absoluto}  Error relativo porcentual: {error_relativo}")


# c) en una serie alternada el error es menor que el primer termino que no se suma
# o sea el error con n terminos es menor que 1/(n+1)
tolerancia = 1e-6

n = 1
while 1 / (n + 1) >= tolerancia:
    n += 1

print(f"\nSe necesitan {n} terminos")

# comprobacion sumando esa cantidad de terminos
suma = 0.0
for i in range(1, n + 1):
    suma += ((-1) ** (i + 1)) / i

error_absoluto = abs(valor_verdadero - suma)
print(f"Suma con {n} terminos: {suma}")
print(f"Error absoluto: {error_absoluto}")