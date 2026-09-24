temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15, 9}

#A) Verificar si la temperatura 9°C se encuentra en ambos sets utilizando condicionales.
for n in temp_max:
    if n == 9:
        for n in temp_min:
            if n == 9:
                print("Se encuentra en ambos sets")

#B) Unir ambos sets en un solo y eliminar duplicados. Imprimir el set generado.

unidos = tuple(temp_min) + tuple(temp_max)
print(set(unidos))

#C) Transformar el set en una lista, y encontrar las temperatura mínima y máxima utilizando bucles. Imprimir los resultados.

temp_max_set = list(unidos)
temp_min_set = list(unidos)

print(max(temp_max_set)) #Imprimiendo resultado
print(min(temp_min_set)) #Imprimiendo resultado

#D) Crear una tupla con los valores de temperaturas mínima y máxima, más un string con las etiquetas de texto: “Mínima” y “Máxima”.
#Imprimir la tupla generada.
temp_tupla_max = (temp_max_set)
temp_tupla_min = (temp_min_set)

tupla_max = print(f"T° maxima '{max(temp_tupla_max)}'")
tupla_min = print(f"T° minima '{min(temp_tupla_min)}'")

#E) Generar e imprimir un diccionario donde las claves sean las temperaturas y los valores sean la frecuencia de aparición.

diccionario = {
    
}