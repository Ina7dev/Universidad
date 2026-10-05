def es_primo(n):
    # solo se prueban divisores hasta la raiz de n
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False  # tiene un divisor, no es primo
        divisor += 1
    return True


# primeros 100 primos
cantidad = 100
lista_primos = []
candidato = 2

while len(lista_primos) < cantidad:
    if es_primo(candidato):
        lista_primos.append(candidato)
    candidato += 1

print(f"Los primeros {cantidad} números primos son:")
print(lista_primos)

# numeros de mersenne, tienen la forma 2^p - 1 con p primo
mersenne_primos = []
mersenne_compuestos = []

print("\nNúmeros de Mersenne con los primeros 10 primos:")
print(f"{'p':>3} {'2^p - 1':>12}   ¿Es primo?")

for p in lista_primos[:10]:
    m = 2**p - 1

    if es_primo(m):
        mersenne_primos.append(m)
        print(f"{p:>3} {m:>12}   Sí")
    else:
        mersenne_compuestos.append(m)
        print(f"{p:>3} {m:>12}   No")

print("\nMersenne que SÍ son primos:", mersenne_primos)
print("Mersenne que NO son primos:", mersenne_compuestos)