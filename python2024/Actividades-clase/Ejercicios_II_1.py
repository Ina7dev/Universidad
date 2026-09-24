mate = (55, 17, 93, 75, 88, 55)
quim = (10, 85, 75, 88, 91, 75)
progra = (68, 78, 85, 68, 82, 10)

materias = ("matematicas", "quimica", "programacion")
puntuacion = (mate, quim, progra)

#A) Imprimir los valores duplicados de cada tupla
for repetida in range(len(materias)):
    asignaturas = materias[repetida] #Obtencion del nombre actual del ramo.
    puntajes = puntuacion[repetida]

    temp = set() #Conjunto donde se guardan los valores unicos
    duplicados = [] #Lista vacia donde se guardan los elementos vacios.

    for j in puntajes:
        if j in temp:
            duplicados.append(j)
        else:
            temp.add(j)
        if duplicados:
            print()
print(duplicados)

# B) Convertir cada tupla en una lista y ordenar las listas en orden descendente
lista_mate = list(mate)
lista_quim = list(mate)
lista_progra = list(mate)

lista_mate.sort(reverse=True)
lista_quim.sort(reverse=True)
lista_progra.sort(reverse=True)
print(f"La lista ordenada de matematicas es de {lista_mate}")
print(f"La lista ordenada de matematicas es de {lista_quim}")
print(f"La lista ordenada de matematicas es de {lista_progra}")

# C) Unir las listas anteriormente generadas en una sola y eliminar los duplicados.
lista = list(set(mate + quim + progra))
print(lista)

# D) Encontrar el puntaje máximo y mínimo de la lista resultante.
maximo = max(lista)
minimo = min(lista)
