"""Crea la clase Coche que contenga las siguientes propiedades:
marca (string): La marca del coche.
gasolina (float): La cantidad de gasolina disponible en el coche.
La clase tendrá un método llamado conducir() que recibirá como argumento el número de kilómetros a
recorrer y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. Por cada 10
kilómetros recorridos, se restará 1 litro de gasolina al valor de la propiedad gasolina. Si la gasolina no es
suficiente para recorrer la distancia solicitada, el coche conducirá solo hasta donde alcance la gasolina y
mostrará un mensaje indicando que se ha quedado sin gasolina.
Además, la clase contendrá otro método llamado cargar_gasolina() que recibirá como argumento los
litros de gasolina que se desean agregar al coche, sumando estos litros al valor de la propiedad gasolina.
"""

class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = gasolina
    

    def conducir(self, kilometros):
        self.kilometros_recorridos = 0
        consumo_gasolina = kilometros / 10
        if consumo_gasolina <= self.gasolina:
            self.kilometros_recorridos += kilometros
            self.gasolina -= consumo_gasolina
            print(f"Has conducido {kilometros} kilómetros. Te queda {self.gasolina:.2f} litros de gasolina.")
        else:
            kilometros_posibles = self.gasolina * 10
            self.kilometros_recorridos += kilometros_posibles
            self.gasolina = 0
            print(f"Te has quedado sin gasolina después de conducir {kilometros_posibles} kilómetros.")

    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Has cargado {litros} litros de gasolina. Ahora tienes {self.gasolina:.2f} litros.")

mi_coche = Coche("Toyota", 10)
mi_coche.conducir(50)  # Conducir 50 kilómetros
mi_coche.cargar_gasolina(5)  # Cargar 5 litros de gasolina
mi_coche.conducir(100)  # Conducir 100 kilómetros
