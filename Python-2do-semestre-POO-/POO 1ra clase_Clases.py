#class Persona():   #Todos los nombres de clase deben llevar mayuscula al principio.
    #Bloque de codigo

    #Atributos

    #Metodos

#Eemplo
class Persona():

    def _init_(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    #Atributos(variables)
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23

    #Metodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} esta hablando")

    def caminar(self):
        print(f"{self.nombre} esta caminando")

#Creacion de un objeto de la clase persona
persona1 = Persona("Cristina", "Torres", 23)
persona2 = Persona("Luis", "Hada", 70)

#Acceso a los atributos y metodos del objeto
print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad} años")

#Llamando a los metodos de la clase
persona1.hablar()
persona2.caminar()
