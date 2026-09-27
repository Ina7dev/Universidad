from math import pi
import numpy as np

n = 10000

suma = np.float32(0.0)  # comienza en 0 y toma decimales

for i in range(1, n + 1):
    suma += np.float32(1) / (np.float32(i) ** 4)

valor_funcionn = (pi ** 4) / 90  # valor verdadero de f(n) cuando n tiende a infinito

error_absoluto = (valor_funcionn - float(suma))
error_relativo = error_absoluto / (valor_funcionn)
error_porcentual = error_relativo * 100

print("----- Suma desde i = 1 hasta 10000 -----")
print(f"Resultado f({n}): {suma}")
print(f"Valor funcion n: {valor_funcionn}")
print(f"Error Absoluto: {error_absoluto}")
print(f"Error Relativo: {error_relativo}")
print(f"Error Relativo Porcentual: {error_porcentual}")


suma_inverso = np.float32(0.0)
for i in range(n, 0, -1):  # ahora desde 10000 hasta 1 con incrementos de -1
    suma_inverso += np.float32(1) / (np.float32(i) ** 4)

error_abs_inverso = (valor_funcionn - float(suma_inverso))
error_rel_inverso = error_abs_inverso / (valor_funcionn)
error_por_inverso = error_rel_inverso * 100

print("\n----- Suma desde i = 10000 hasta 1 -----")
print(f"Resultado f({n}): {suma_inverso}")
print(f"Valor funcion n: {valor_funcionn}")
print(f"Error Absoluto: {error_abs_inverso}")
print(f"Error Relativo: {error_rel_inverso}")
print(f"Error Relativo Porcentual: {error_por_inverso}")