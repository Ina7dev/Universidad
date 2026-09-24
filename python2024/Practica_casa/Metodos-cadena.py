cadena1= "Hola, soy Ina"
cadena2 = "123345"

#Convierte todo a mayusculas
cadena3 = cadena1.upper()
print(cadena3)

#Convierte todo a minusculas
cadena4 = cadena1.lower()
print(cadena4)

#Convierte todo a minusculas menos la primer letra
cadena5 = cadena1.capitalize()
print(cadena5)

#Buscar una cadena dentro de otra cadena #/cuando no encuentra un valor arroja "-1"
busqueda_cadena = cadena1.find("Hola")
busqueda_cadena = cadena1.index("Hola") #Cuando no encuentra un valor arroja una excepcion
print(busqueda_cadena)

#Si es numerico arroja True, sino arroja False
cadena_numerico = cadena1.isnumeric()
cadena_numerico2 = cadena2.isnumeric()
print(cadena_numerico)
print(cadena_numerico2)


#Si es alfanumerico arroja True, sino False
cadena_alfanumerico = cadena1.isalpha()
print(cadena_alfanumerico) #Arroja False pq el texto tiene espacio, y el espacio es caracter especial, los alfanumericos son de la a-z

#Buscamos la cantidad de coincidencias de una cadena dentro de otra cadena
cadena_contar = cadena1.count("Hola") #Cuenta las veces que sale "Hola" en el texto.
print(cadena_contar)

#Cuenta la cantidad de caracteres que tiene un texto
cadena_cantidad = len(cadena1)
print(cadena_cantidad)

#Verifica si una cadena empieza por otra cadena, si es asi devuelve True
cadena_empieza = cadena1.startswith("H") #Arroja True pq la cadena comienza con H.
print(cadena_empieza)

#Verifica si una cadena termina por otra cadena, si es asi devuelve True
cadena_termina = cadena1.endswith("a") #Arroja True pq la cadena termina con a.
print(cadena_termina)

#Reemplaza un pedazo de cadena dada por otra dada.
cadena_nueva = cadena1.replace("Hola", "Lu") #La primera cadena debe ser parte del texto y lo que va despues de la coma, el nuevo valor
print(cadena_nueva)

#Separa cadenas con la cadena que le pasemos
cadena_separada = cadena1.split()
print(cadena_separada)