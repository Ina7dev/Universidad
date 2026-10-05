import math

aureo = (1 + math.sqrt(5)) / 2

a = 1
b = 1
fibonacci = [a, b]
divisiones = []

# se sigue generando la serie hasta que la division de igual al numero aureo
while b / a != aureo:
    a, b = b, a + b
    fibonacci.append(b)
    divisiones.append(b / a)

print("Numero aureo:", aureo)
print("Serie de Fibonacci:", fibonacci)
print("Cantidad de numeros que se necesitaron:", len(fibonacci))
print("Divisiones:", divisiones)
print("Ultima division:", divisiones[-1])