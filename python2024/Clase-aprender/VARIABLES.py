edad = 30
estatura = 1.71 #declarando numero decimal
n_comp = 5 + 4j
n_comp2 = complex (5,4)

#FORMATO DE SALIDA NUMERICA (FLOTANTES)


pi = 3.14159
print ("PI: ", round (pi,2)) #funcion round
print(f"PI: {pi:.2f}") #formato f-string


#IMPRESIÓN DE VARIABLE (CONCATENACIÓN)

name = "Valentina"
apellido = "Calderón"
edad = 21

print("Hola soy " + name + " " + apellido + " y tengo " + str(edad) + " años");
print(f"Mi nombre es {name} {apellido} y tengo {edad} años")


#VARIABLES DE UNA LINEA

pais, region, ciudad, codigo_postal= "Chile", "Los lagos", "Castro", 5700000
print(pais, region, ciudad, codigo_postal)
print(pais + region + ciudad + str(codigo_postal))



#UTILIZANDO INPUT
año = input("¿En que año naciste?")
print("El año de nacimineto ingresado es: " , año)