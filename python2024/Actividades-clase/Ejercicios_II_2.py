"""Desarrollar un algoritmo que solicite al usuario una cadena de texto y cuente cuántas veces
aparecen las vocales 'a', 'e', 'i', 'o' y 'u' en la cadena de texto. Utilizar ciclos para resolver el
problema.
"""

texto = input("Ingrese un texto: ").lower()

#Inicializar contadores para cada vocal

contador_a =0
contador_e =0
contador_i =0
contador_o =0
contador_u =0

#Iterar sobre cada caracter
for caracter in texto:
    if caracter == 'a':
        contador_a += 1
    elif caracter == 'e':
        contador_e += 1
    elif caracter == 'i':
        contador_i += 1
    elif caracter == 'o':
        contador_o += 1
    elif caracter == 'u':
        contador_u += 1

# Mostrar el contador de cada vocal
print(f"La vocal 'a' aparece {contador_a} veces en la cadena de texto.")
print(f"La vocal 'e' aparece {contador_e} veces en la cadena de texto.")
print(f"La vocal 'i' aparece {contador_i} veces en la cadena de texto.")
print(f"La vocal 'o' aparece {contador_o} veces en la cadena de texto.")
print(f"La vocal 'u' aparece {contador_u} veces en la cadena de texto.")