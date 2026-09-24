class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando... ")
    
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
grado = int(input("Ingrese su grado: "))

estudiante_1 = Estudiante(nombre, edad, grado)
print(f"El estudinate se llama {estudiante_1.nombre} tiene {estudiante_1.edad} años y va en {estudiante_1.grado} grado")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante_1.estudiar()
        break