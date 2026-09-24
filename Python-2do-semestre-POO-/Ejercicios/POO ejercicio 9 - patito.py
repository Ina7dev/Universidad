import math

#Definición de las clases para las figuras geométricas
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Trapecio:
    def __init__(self, base_menor, base_mayor, altura):
        self.base_menor = base_menor
        self.base_mayor = base_mayor
        self.altura = altura

    def calcular_area(self):
        return ((self.base_menor + self.base_mayor) * self.altura) / 2

class PentagonoRegular:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def calcular_area(self):
        perimetro = 5 * self.lado
        return (perimetro * self.apotema) / 2

#Función para mostrar el área de cualquier figura geométrica
def mostrar_area(figura):
    try:
        area = figura.calcular_area()
        print(f"El área de la figura es: {area}")
    except AttributeError:
        print("La figura no tiene un método calcular_area()")

#uso
if __name__ == "__main__":
    figuras = [
        Circulo(5),
        Rectangulo(10, 4),
        Triangulo(6, 3),
        Cuadrado(4),
        Trapecio(3, 5, 4),
        PentagonoRegular(6, 4)
    ]

    for figura in figuras:
        mostrar_area(figura)