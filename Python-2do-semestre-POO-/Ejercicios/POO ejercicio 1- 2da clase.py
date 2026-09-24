#Ejercicio 1

class Persona():

    def _init_(self, nombre, apellido, edad, altura, peso, nota1, nota2, nota3):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura 
        self.peso = peso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    #Atributos(variables)
    #nombre = "Cristina"
    #apellido = "Torres"
    #edad = 23

    #Metodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} esta hablando")

    def caminar(self):
        print(f"{self.nombre} esta caminando")

    def calculo_imc(self):
        print(f"Su IMC es de {self.peso/self.altura**2}")
        if (self.peso/self.altura**2) < 18.5:
            print(f"Su IMC se encuentra dentro del rango de bajo peso")
        elif (self.peso/self.altura**2) >= 18.5 and (self.peso/self.altura**2) < 25:
            print(f"Segun su IMC se encuentra normal")
        elif (self.peso/self.altura**2) >= 25 and (self.peso/self.altura**2) < 35:
            print(f"Su IMC se encuentra dentro del rango de obesidad")
        else:
            print(f"Segun su IMC se encuentra dentro del rango obesidad")

    def promedio_asignatura(self):
        print(f"El promedio es {(self.nota1+self.nota2+self.nota3/3)}")
        if ((self.nota1+self.nota2+self.nota3/3)) > 4:
            print("Asignatura aprobada C:")
        else:
            print("Asignatura reprobada")


#Creacion de un objeto de la clase persona
persona1 = Persona("Cristina", "Torres", 23, 1.65, 55, 5.5, 6, 5)

#Acceso a los atributos y metodos del objeto
print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad} años")
print(f"{persona1.altura}m")
print(f"{persona1.peso}kg")
print(f"{persona1.nota1}")
print(f"{persona1.nota2}")
print(f"{persona1.nota3}")

#Llamando a los metodos de la clase
persona1.hablar()
persona1.calculo_imc()
persona1.promedio_asignatura()
