#STRINGS

institucion = "Universidad de Los Lagos"
asignatura = 'Programación'
descripcion = """asignatura de primer semestre
de la carrera de Ingeniería Civil en Informática"""


#IMPRIME LA POSICIÓN DE UN CARACTER
print(institucion[-2])

#CONCATENACIÓN
resultado = print(institucion + " " + asignatura)

#MULTIPLICACIÓN POR TEXTO
salida = print(institucion * 4)

#UTILIZANDO LA FUNCION SPLIT
print(institucion.split())

print(len(asignatura))

#LISTAS

ciudades = ["Castro", "Queilen", "Ancud", "Quellón", "Chonchi", "Castro"]
varios = ["Nicolas", 20, True]

list()
print(type(ciudades))
print(ciudades)

print(len(ciudades)) #cuenta la cantidad de elementos de una lista

print(ciudades.count("Castro")) #cuenta la cantidad de ocurrencias de una lista



listn2 = list(range(1,1001,10)) #Crea una lista que cominece desde el 1 hasta el 1000

print(listn2)


#Impresion de un elemnto en especifico de una lista
print(ciudades[3])

ciudades[0] = "Quemchi" #Otorga una nueva posicion a un elemento de la lista.
print(ciudades)

# TUPLAS

basica = tuple()
generos = ("rock", "Blues", "Pop", "Trap", "HipHop")
print(generos)
print(type(generos))

print(generos[2])
print(generos.index("Pop")) #Consulta la posicion de un elemento especifico.

tup = ("Victor", 200, "Universidad", True)
print(tup)
tup = list(tup)
print(f"La tupla ahora es de tipo {type(tup)}")

#Tomando un trozo de una tupla.
print(tup[0:3])

#Conjuntos
c_v1 = set() #Inicializando un Set
print(type(c_v1)) #(Las llaves sirven paa sets y diccionarios)
c_v = {"JavaScript"}
print(type(c_v))
c_v2 = { }
print(type(c_v2))

#Inicializando Sets
colores = {"Azul", "Rojo", "Amarillo", "Verde", "Morado"}
animales = set({"Gato", "Perro", "Caballo", "Hamster"})
print(colores)
print(animales)

colores.add("Celeste") #No se puede darle un orden.
print(colores)

#Diccionarios
paciente = dict(    
    nombre = "Francisco",
    edad = 30,
    ciudad = "Castro"
)

doctor = {
    "nombre" : "Elson",
    "edad" : 40,
    "especialidad" : "Cirujano"}
print(doctor, paciente)
#Eliminando la clave "nombre"
doctor.pop("nombre")
print("Diccionario actualizado: ", doctor)

print(paciente.keys())
print(paciente.values())

#Consultar valores especificos.
print(paciente["nombre"])

#Actualizar dicccinarios
paciente.update()

#Map
n = [1, 2, 3, 4, 5]
nt = list(map(str,n))
print(f"La lista de numeros como string {", ".join(nt)}")

#filter
r = ["Programación", "Taller", "Matemáticas", "Física", "Inglés"]
l = list(filter(lambda x: len(x) > 7, r))
print(l)

#Zip.    Queda con solo la cantidad elementos que tengan en comun
a = [1,2,3,4]
b = ["A", "B", "C", "D"]
com = list(zip(a,b)) 
print(com)