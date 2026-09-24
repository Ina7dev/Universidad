class Pedido:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.platos = []
        self.total = 0
    
    def añadir_plato(self, nombre, precio):
        self.platos.append((nombre, precio))
        self.total += precio
    
    def calcular_total(self):
        return self.total
    
    def __len__(self):
        return len(self.platos)
    
    def __add__(self, otro):
        nuevo_pedido = Pedido(self.numero_mesa)
        nuevo_pedido.platos = self.platos + otro.platos
        nuevo_pedido.total = self.total + otro.total
        return nuevo_pedido
    
    def finalizar(self):
        print(f"El pedido de la mesa {self.numero_mesa} ha sido completado.")   

    def __del__(self):
        self.finalizar()


    # Crear un pedido para la mesa 1
pedido1 = Pedido(numero_mesa=1)
pedido1.añadir_plato("Pizza :v", 12000)
pedido1.añadir_plato("Ensalada", 4000)
    
    # Crear otro pedido para la misma mesa 
pedido2 = Pedido(numero_mesa=1)
pedido2.añadir_plato("Tallarines con carne", 7000)
    
print(f"Total del pedido 1: ${pedido1.calcular_total()}")
print(f"Total del pedido 2: ${pedido2.calcular_total()}")
    
    # Contar el número de platos en el pedido
print(f"Número de platos en el pedido 1: {len(pedido1)}")
    
    # Combinar los dos pedidos
pedido_combinado = pedido1 + pedido2
print(f"Total del pedido combinado: ${pedido_combinado.calcular_total()}")
    
    # Mostrar el número de platos del pedido combinado
print(f"Número de platos en el pedido combinado: {len(pedido_combinado)}")
    
del pedido2
