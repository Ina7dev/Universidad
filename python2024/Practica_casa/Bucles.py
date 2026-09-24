#Ingresar un N° por consola, y si el n es mayor se dice y lo mismo con menor, hasta que se adivina el n.
#FORMA 1
numero_colocado = int(input("Ingresa un N°: "))

"""while True:
    num_adivinar = int(input("Ingresa un numero a adivinar: "))
    if numero_colocado > num_adivinar:
        print("El N° es menor")
    elif numero_colocado < num_adivinar:
        print("El N° es mayor")
    else:
        print("Has adivinado el N°")
        break"""


#vocales
#solicita texto, contar cuantas veces salen las vocales, utilizar ciclos.

"""texto = input("Ingresa un texto: ").lower()

letra_a = 0
letra_e = 0
letra_i = 0
letra_o = 0
letra_u = 0

for vocal in texto:
    if vocal == "a":
        letra_a += 1
    elif vocal == "e":
        letra_e += 1
    elif vocal == "i":
        letra_i += 1
    elif vocal == "o":
        letra_o += 1
    elif vocal == "u":
        letra_u += 1

print(f"Las veces que se repitio la vocal 'a' es de {letra_a}")
print(f"Las veces que se repitio la vocal 'e' es de {letra_e}")
print(f"Las veces que se repitio la vocal 'i' es de {letra_i}")
print(f"Las veces que se repitio la vocal 'o' es de {letra_o}")
print(f"Las veces que se repitio la vocal 'u' es de {letra_u}")"""

#Ingresar lista de cadenas invertir con ciclos.

"""texto = input("Ingresa un texto: ")
si = " "

for i in texto[::-1]:
    si += i
print(si)"""

#
#A
def aprendiendo(poronga):
    lista = []
    conjunto = {}
    for i in poronga:
        if i in conjunto:
            conjunto[i] += 1
        else:
            conjunto[i] = 1
    for clave, valor in conjunto.items():
        if valor > 1:
            lista.append(clave)
    return lista

mate = (55,17,93,75,88,55)
quim = (10,85,75,88,91,75)
progra = (68,78,85,68,82,10)

lista_mate = list(mate)
lista_quim = list(quim)
lista_progra = list(progra)

print(aprendiendo(lista_mate))
print(aprendiendo(lista_quim))
print(aprendiendo(lista_progra))


#B
lista_mate = list(mate)
lista_quim = list(quim)
lista_progra = list(progra)

lista_mate.sort()
lista_quim.sort()
lista_progra.sort()
