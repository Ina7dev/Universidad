valor_verdadero = 0.69314718056  # ln(2) el enunciado

# a) y b) Sumas parciales S4 a S8
print("a) y b) Sumas parciales y errores")
print(f"{'n':>3} {'S_n':>14} {'Error absoluto':>16} {'Error relativo %':>17}")

suma = 0.0
for n in range(1, 9):
    termino = ((-1) ** (n + 1)) / n
    suma += termino

    if n >= 4:  # solo pide desde S4 hasta S8
        error_absoluto = abs(valor_verdadero - suma)
        error_relativo = error_absoluto / valor_verdadero * 100
        print(f"{n:>3} {suma:>14.10f} {error_absoluto:>16.10f} {error_relativo:>17.6f}")


# términos para error absoluto < 10^-6
# En una serie alternada el error queda acotado por el primer término que no se sumó 
# |ln(2) - S_n| <= 1/(n+1)
tolerancia = 1e-6

n = 1
while 1 / (n + 1) >= tolerancia:
    n += 1

print(f"\nc) Según la cota de la serie alternada se necesitan n = {n} términos")

# sse suma los términos y se ve el error real
suma = 0.0
for i in range(1, n + 1):
    suma += ((-1) ** (i + 1)) / i

error_real = abs(valor_verdadero - suma)
print(f"S_{n} = {suma:.12f}")
print(f"Error absoluto real = {error_real:.4e}  (cota: 1/(n+1) = {1/(n+1):.4e})")