class Animal(): # super clase / clase general
    def __init__(self,nombre,edad,peso,color,sonido):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
        self.sonido = sonido

    def comer(self):
        print(f"{self.name} está comiendo")

    def hacer_sonido(self):
        print(self.sonido)
    
class Perro(Animal):
    def __init__(self, nombre, edad, raza, peso, color, sonido):
        super().__init__(nombre, edad, peso, color, sonido)
        self.raza = raza
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando")


    def info(self):
        print("Informacion del Perro: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n raza: {self.raza} \n peso: {self.peso} \n color: {self.color} \n sonido: {self.sonido} \n ")

class Gato(Animal):
    def __init__(self, nombre, edad, saltar_Alto, peso, color, sonido):
        super().__init__(nombre, edad, peso, color, sonido)
        self.saltar_alto = saltar_Alto

    def maullar(self):
        print(f"{self.nombre} está maullando")

    def info(self):
        print("Informacion del Gato: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n salta una altura de: {self.saltar_alto} \n peso: {self.peso} \n color: {self.color} \n sonido: {self.sonido} \n ")


class Loro(Animal):
    def __init__(self, nombre, edad, plumaje, peso, color, sonido):
        super().__init__(nombre, edad, peso, color, sonido)
        self.plumaje = plumaje 
        
    def volar(self):
        print(f"{self.nombre} está volando")
        
    def info(self):
        print("Informacion del Loro: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n con plumaje: {self.plumaje} \n peso: {self.peso} \n color: {self.color} \n sonido: {self.sonido} \n ")
    

class Pez(Animal):
    def __init__(self, nombre, edad, peso, color, sonido, especie):
        super().__init__(nombre, edad, peso, color, sonido)
        self.especie = especie
        
    def nadar(self):
        print(f"El pez {self.name}")
    
    def info(self):
        print("Informacion del Pez: \n")
        print(f"Nombre: {self.nombre} \n edad: {self.edad} \n Especie: {self.especie} \n peso: {self.peso} \n color: {self.color} \n sonido: {self.sonido} \n ")

perro1 = Perro("Niebla", 3, "Quiltrometro", 11, "Amarillo", "Guau")
gato1 = Gato("Michihausen", 2, 2, 5, "Blanco y gris", "Rauuul")
pajaro1 = Loro("Pepe", 35, "Abundante", 2, "verde", "coco")
pez1 = Pez("Rogelio", 6, 500, "gris", "GRRR", "Pez espada")

perro1.info()
gato1.info()
pajaro1.info()
pez1.info()