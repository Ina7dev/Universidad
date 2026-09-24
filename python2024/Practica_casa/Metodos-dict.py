diccionario = {
    "nombre" : "ina",
    "apellido" : "calderon",
    "edad" : 21
}

claves = diccionario.keys() #Muestra las claves, o sea, el lado izquierdo
print(claves)

valor = diccionario.get("nombre") #Muestra el valor de la clave
print(valor)

diccionario.pop("nombre") #Borra el elemento escogido
print(diccionario)

diccionario_iterable = diccionario.items() #Recorre los elementos
print(diccionario_iterable)

diccionario.clear() #Borra todo
print(diccionario)