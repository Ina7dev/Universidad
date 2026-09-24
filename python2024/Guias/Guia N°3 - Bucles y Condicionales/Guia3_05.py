#5
import random

n = [random.randint(40, 350) for _ in range(20)]

print("Lista de números generada:")
print(n)

nbuscar = int(input("Ingrese el número que desea buscar en la lista: "))

nrepetidos = n.count(nbuscar)

print(f"El número {nbuscar} aparece {nrepetidos} veces en la lista.")