#por terminal pedir breve resumen del artículo igual o menor a 60 caracteres.
br = input("Ingrese un breve resumen, puede ser menor o igual a 60 caracteres: ")
#variable booleana, True si la longitud es igual o menor a 60 caracteres y False en caso contrario.
l = len(br) <= 60
print(l)
#Imprimir la longitud de caracteres del breve resumen del artículo

#Convertir el resumen en mayúsculas utilizando la función de Python adecuada.
br_m = br.upper()
print(f"El resumen en mayusculas es {br_m}")
#Mostrar los últimos diez caracteres del resumen
b = br[:10]
b1 = max(b)
print(f"Los ultimos 10 caracteres del resumen son: {b}")
print(f"Los ultimos 10 caracteres del resumen son: {b1}")
#Unir las palabras del resumen con un guión (-) como separador utilizando la función correcta.
br_mj = "-".join(br_m.split())
print(f"El resumen en mayusculas y con - seria: {br_mj}")