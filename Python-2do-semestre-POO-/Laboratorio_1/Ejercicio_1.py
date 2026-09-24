#Implementar la clase Personaje con los atributos y métodos descritos anteriormente
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre     
        self.vida = vida       
        self.ataque = ataque   
    
    def atacar(self, otro_personaje):
 
        if self.esta_vivo() and otro_personaje.esta_vivo():
            print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {self.ataque} puntos de daño.\n")
            otro_personaje.vida -= self.ataque
            if otro_personaje.vida < 0:
                otro_personaje.vida = 0
        else:
            print(f"{self.nombre} o {otro_personaje.nombre} no están en condiciones de seguir luchando.\n")
    
    def esta_vivo(self):
        return self.vida > 0
    
    def __str__(self):
        return f"Personaje: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}\n"

#Crear al menos dos personajes. Cada personaje debe tener un nombre, vida inicial y puntos de ataque
personaje1 = Personaje("Ina", 50, 15)
personaje2 = Personaje("Dobby", 60, 10)

#Simula un combate entre los personajes haciendo que uno ataque al otro. Después de cada ataque, se debe mostrar el estado de ambos personajes.
#Repetir los ataques hasta que uno de los personajes quede sin vida. Utiliza un método para verificar si el personaje sigue en pie.

while personaje1.esta_vivo() and personaje2.esta_vivo():
    personaje1.atacar(personaje2)
    print(personaje1)
    print(personaje2)
    
    if not personaje2.esta_vivo():
        print(f"{personaje2.nombre} ha muerto.\n")
        break
    
    personaje2.atacar(personaje1)
    print(personaje1)
    print(personaje2)
    
    if not personaje1.esta_vivo():
        print(f"{personaje1.nombre} ha muerto.\n")