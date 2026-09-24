"""Encapsulación y Atributos Privados"""
#1. Encapsulación de Datos del Cliente
"""A) 1.-Deberian encapsularse los datos del tipo de cliente, el precio de la compra, el
    2-3.- Deberia ser privado el precio de la compra, porque """
class Cliente:
    _descuentos = {
        "estudiante": 0.2,
        "Academico": 0.1,
        "otro": 0.0
        } #Se utilizo el diccionario privado por comodidad, aunque igual servian otros metodos, como una lista, por ejemplo.
    def __init__(self, tipo_cliente, precio_compra):
        assert tipo_cliente in ["estudiante", "academico", "otro"], "Tipo de cliente no válido"
        self._tipo_cliente = tipo_cliente
        assert precio_compra >= 0, "El precio de la compra no puede ser negativo, ingrese un monto positivo."
        self._precio_compra = precio_compra


    def get_precio_compra(self): #para el precio de la compra
        return self.__precio_compra

    def set_precio__nuevo_compra(self, nuevo_precio):
        assert nuevo_precio >= 0, "El precio no puede ser negativo, ingrese un monto positivo"
        self.__precio_compra = nuevo_precio

    def get_precio_final(self):
        descuento = Cliente.__descuentos[self.__tipo_cliente]
        return self.__precio_compra * (1 - descuento)
    
    @staticmethod
    def calcular_precio_final(tipo_cliente, precio_compra):
        assert tipo_cliente in ["estudiante", "academico", "otro"], "Tipo de cliente no válido"
        assert precio_compra >= 0, "El precio de la compra no puede ser negativo"
        descuento = Cliente.__descuentos[tipo_cliente]
        return precio_compra * (1 - descuento)
    
    def get_tipo_cliente(self):
        return self.__tipo_cliente
    
    def set_tipo_cliente(self, nuevo_tipo_cliente):
        assert nuevo_tipo_cliente in ["estudiante", "academico", "otro"], "Tipo de cliente no válido"
        self.__tipo_cliente = nuevo_tipo_cliente


"""Respuestas
1. Encapsulación de Datos del Cliente
A) ¿Qué datos del cliente crees que deben encapsularse en una clase Cliente?, El tipo de cliente, el precio de la compra.
    ¿Cuál de estos atributos debería ser privado y cuál público? ¿Por qué?, Se dejo privado el precio de la compra,
    porque es privado lo que pagan :|
2.-
¿Cómo organizarías los descuentos disponibles para cada tipo de cliente en
el sistema? ¿Crees que un diccionario privado podría ser útil para almacenar
los descuentos para cada tipo de cliente? ¿o se necesita otro tipo de
estructura de datos?
r: si, tanto un diccionario como una lista podrian haber servido. Aqui se utilizo el diccionario privado.
"""

