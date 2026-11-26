import math

x = int(input("Ingresa a que potencia quieres elevar e: "))
n = int(input("Ingresa la cantidad de terminos: "))

factoriales = []
suma = 0

# e^x = 1 + x + x^2/2! + x^3/3! + ...
for i in range(n):
    fact = math.factorial(i)
    factoriales.append(fact)
    suma += x**i / fact

valor_real = math.exp(x)
error = abs(valor_real - suma) / valor_real * 100

print("Factoriales usados:", factoriales)
print(f"e^{x} con {n} terminos = {suma}")
print(f"Valor real = {valor_real}")
print(f"Error porcentual = {error}%")