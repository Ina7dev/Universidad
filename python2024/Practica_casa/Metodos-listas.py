#Creando una lista con list
lista = list(["Hola", "Ina", 21])
lista2 = [21,2024, True, 2003,False]
lista22 = [21,2024, 2003,False]
print(lista)

#Dice la cantidad de elementos en una lista
lista_contar = len(lista)
print(lista_contar)

#Agregando un elemento a la lista
lista_agregando = lista.append("ULagos")
print(lista_agregando)

#Agregando un elemento a la lista desde un lugar en especifico
lista_agre_especifico = lista.insert(1, "ULagos")#El primer digito es la posicion y lo segundo el valor a cambiar

#Agregar varios elementos a la lista
lista.extend([False, 2024])

#Eliminando un elemento de la lista por su indice
lista.pop(0)
print(lista)

#Removiendo un elemento de la listapor su valor
lista.remove("Ina")
print(lista)

#Eliminar todos los elementos de la lista
lista.clear()
print(lista)

#Ordenando una lista. (Menor a mayor)
lista2.sort()
print(lista2)

#Ordenando una lista al reves (mayor a menor)
lista2.sort(reverse=True)
print(lista2)

#Verificar donde se encuentra un elemento
lista_encontrar = lista2.index(21)
print(lista_encontrar)