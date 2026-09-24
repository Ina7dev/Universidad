"""Determinar si una palabra ingresada por teclado es un palíndromo. Eliminar espacios y
convertir el texto ingresado a minúsculas. Además, imprimir la palabra invertida"""

palindromo = input("Ingresa una palabra para saber si palindromo: ").lower()

eliminar_espacio = "".join(palindromo.split())

palabra_alreves = eliminar_espacio[::-1]

print(palabra_alreves)
print("""Si la palabra ingresada se puede leer igual al reves es palindromo.
Si no se puede leer exactamente igual, no es palindromo""")

lista = []
for i in palabra_alreves:
    if i == palabra_alreves(reversed=True):  #Se trato de utilir if para saber si es palindromo
        lista[i] = palabra_alreves