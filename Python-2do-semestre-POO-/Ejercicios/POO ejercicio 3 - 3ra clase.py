"""Implementar una clase Fraccion que represente una fracción matemática con numerador y
denominador. Además se debe crear varios métodos mágicos que permitan operar, comparar, y mostrar
las fracciones de manera intuitiva. La clase debe poseer los siguientes métodos mágicos:
Método mágico que devuelva la fracción como una representación de cadena
Método mágico que permita sumar dos fracciones
Método mágico que permita el producto entre dos fracciones
Método mágico que permita comparar dos fracciones. Dos fracciones se consideran iguales si sus
valores numéricos son equivalentes."""

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    #Fraccion como cadena.
    def __str__ (self):
        return f"{self.numerador}/{self.denominador}"
    
    #Fraccion sumadas.
    def __add__(self):

    #Fraccion multiplicadas.


    #Comparar dos fracciones.

fraccion1 = Fraccion(1,2)
fraccion2 = Fraccion(3,5)

print(fraccion1)