from math import sqrt

a = 10
valor_verdadero = sqrt(a)
error_tolerado = 0.5 * 10 ** (2 - 6)  # para 6 cifras significativas, en porcentaje

print(f"Valor verdadero: {valor_verdadero}")

# a) 4 iteraciones partiendo de x0 = 3
print("\na) x0 = 3")
x = 3
for i in range(4):
    x = 0.5 * (x + a / x)
    error_verdadero = abs((valor_verdadero - x) / valor_verdadero) * 100
    print(f"Iteracion {i + 1}: {x}  Error verdadero: {error_verdadero}")


# b) se itera hasta que el error sea menor al tolerado
print("\nb) iteraciones para 6 cifras con x0 = 3")
x = 3
iteraciones = 0
error_verdadero = 100

while error_verdadero >= error_tolerado:
    x = 0.5 * (x + a / x)
    iteraciones += 1
    error_verdadero = abs((valor_verdadero - x) / valor_verdadero) * 100
    print(f"Iteracion {iteraciones}: {x}  Error verdadero: {error_verdadero}")

print(f"Se necesitaron {iteraciones} iteraciones")


# c) lo mismo pero ahora con x0 = 10
print("\nc) iteraciones para 6 cifras con x0 = 10")
x = 10
iteraciones = 0
error_verdadero = 100

while error_verdadero >= error_tolerado:
    x = 0.5 * (x + a / x)
    iteraciones += 1
    error_verdadero = abs((valor_verdadero - x) / valor_verdadero) * 100
    print(f"Iteracion {iteraciones}: {x}  Error verdadero: {error_verdadero}")

print(f"Se necesitaron {iteraciones} iteraciones")