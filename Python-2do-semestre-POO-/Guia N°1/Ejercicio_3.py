class Producto:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial_stock = []
    def actualizar_stock(self, cantidad):
        if cantidad > 0:
            self.historial_stock.append(f'Incremento: {cantidad}')
        elif cantidad < 0:
            self.historial_stock.append(f'Decremento: {cantidad}')
        self.cantidad += cantidad
    def valor_total(self):
        return self.cantidad * self.precio
    def __str__(self):
        return (f'Nombre: {self.nombre}\n'
                f'Precio por unidad: ${self.precio:.2f}\n'
                f'Cantidad disponible: {self.cantidad}\n'
                f'Código: {self.codigo}\n'
                f'Historial de stock: {self.historial_stock}')
class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            raise ValueError('El producto ya está en el inventario')
        self.productos[producto.codigo] = producto
    def actualizar_stock_producto(self, codigo, cantidad):
        if codigo not in self.productos:
            raise KeyError('El producto no se encuentra en el inventario.')
        self.productos[codigo].actualizar_stock(cantidad)
    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)
            print('---')
    def valor_total_inventario(self):
        return sum(producto.valor_total() for producto in self.productos.values())
producto1 = Producto('Laptop', 1500.00, 10, '001')
producto2 = Producto('Mouse', 25.00, 50, '002')
inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.actualizar_stock_producto('001', -2)
inventario.actualizar_stock_producto('002', 10)
inventario.mostrar_productos()
print(f'Valor total del inventario: ${inventario.valor_total_inventario():.2f}')