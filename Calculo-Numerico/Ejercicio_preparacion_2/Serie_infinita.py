from math import pi

n = 10000

suma = 0.0 # comienza en 0 y toma decimales

for i in range(1, n + 1):
    suma += 1 / (i ** 4)
    
valor_funcionn= (pi ** 4) / 90 #valor de f(n)


error_absoluto = (valor_funcionn - suma)
error_relativo = error_absoluto / (valor_funcionn)
error_porcentual = error_relativo * 100

print(f"Resultado f({n}): {suma}")
print(f"Valor funcion n: {valor_funcionn}")

print(f"Error Absoluto: {error_absoluto}")
print(f"Error Relativo: {error_relativo}")
print(f"Error Relativo Porcentual: {error_porcentual}")


suma_inverso = 0.0
for i in range(n, 0, -1):
    suma_inverso += 1 / (i ** 4)
    
error_abs_inverso = (valor_funcionn - suma_inverso)
error_rel_inverso = error_abs_inverso / (valor_funcionn)
error_por_inverso = error_rel_inverso * 100

print(f"Resultado f({n}): {suma_inverso}")
print(f"Valor funcion n: {valor_funcionn}")

print(f"Error Absoluto: {error_abs_inverso}")
print(f"Error Relativo: {error_rel_inverso}")
print(f"Error Relativo Porcentual: {error_por_inverso}")
