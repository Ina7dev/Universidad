### Encapsulación y Variables de Instancia:
### La clase debe contener las siguientes variables de instancia privadas:
### Nombre de la cafetería.
### Un menú con el nombre del producto como clave y su precio como valor.
### Una lista de pedidos para almacenar los productos solicitados por los clientes.
class Cafeteria:
    descuento = 10  # 10%

    def __init__(self, nombre):
        self.__nombre = nombre  
        self.__menu = {}  
        self.__pedidos = []  

    def agregar_producto(self, nombre, precio):
        assert precio > 0, "El precio debe de ser mayor que 0"
        assert nombre not in self.__menu, "El producto ya existe en el menú."
        self.__menu[nombre] = precio

    def agregar_pedido(self, producto):
        assert producto in self.__menu, "El producto no está en el menú."
        self.__pedidos.append(producto)

    def calcular_total(self, frecuente = False):
        total = 0 
        for producto in self.__pedidos:
            total += self.__menu[producto]  
        if frecuente:
            descuento = total * Cafeteria.descuento // 100  
            total -= descuento  
        return total

    @staticmethod
    def calcular_precio_descuento(monto, descuento):
        assert monto >= 0, "El monto debe ser mayor que 0"
        assert 0 <= descuento <= 100, "El descuento debe estar entre 0 y 100."
        return monto * (descuento / 100)

    def mostrar_menu(self):
        return self.__menu   ##no me funciono el metodo str

    def mostrar_pedidos(self):
        return self.__pedidos


##nombrar la cafeteria (como mi gato)
cafeteria = Cafeteria("Café Michihausen")
print(f"Bienvenidos a la Cafeteria {cafeteria} revise nuestro menú e ingrese su orden: ")


##agregar los porductos disponibles para el menu c:
cafeteria.agregar_producto("Café", 2500)
cafeteria.agregar_producto("Torta", 4000)
cafeteria.agregar_producto("Rollitos de Canela", 3000)
cafeteria.agregar_producto("Té verde", 2000)
cafeteria.agregar_producto("Muffins", 2000)
print(f"Menú:", cafeteria.mostrar_menu())
    
##agregar los pedidos c: 
cafeteria.agregar_pedido("Café")
cafeteria.agregar_pedido("Torta")
cafeteria.agregar_pedido("Té verde")
##precios para cliente frecuente
total_pedido = cafeteria.calcular_total(frecuente=True)
total_pedido1 = cafeteria.calcular_total(frecuente=False)
precio_descuento_Especial = cafeteria.calcular_precio_descuento(total_pedido1, 50)

print(f"Total del pedido con su descuento cliente frecuente! : ${total_pedido} antiguamente el valor de su pedido era de ${total_pedido1} disfrute su orden.")
print(f"Haz ganado la promoción del descuento especial, tu precio del pedido ahora es de {precio_descuento_Especial}")
    

print(f"Pedidos por entregar:", cafeteria.mostrar_pedidos())