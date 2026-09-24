class SistemaDeVentaDeTickets:
    descuento_grupo = 0.20

    precios_tickets = {}
    ventas_registradas = []

    @classmethod
    def agregar_tipo_ticket(cls, tipo, precio):
        assert precio > 0, "El precio debe ser positivo."
        cls.precios_tickets[tipo] = precio

    @classmethod
    def registrar_venta(cls, tipo_ticket, cantidad):
        assert tipo_ticket in cls.precios_tickets, "El tipo de ticket no existe."
        assert cantidad > 0, "La cantidad debe ser positiva."

        precio = cls.precios_tickets[tipo_ticket]
        total_venta = cls.calcular_total_venta(precio, cantidad)
        cls.ventas_registradas.append(total_venta)

    @classmethod
    def calcular_total_venta(cls, precio, cantidad):
        total = precio * cantidad
        if cantidad > 5:
            total -= total * cls.descuento_grupo
        return total

    @classmethod
    def calcular_ingresos_totales(cls):
        return sum(cls.ventas_registradas)

    @classmethod
    def mostrar_precios_tickets(cls):
        print("Precios de Tickets:")
        for tipo, precio in cls.precios_tickets.items():
            print(f"Tipo: {tipo}, Precio: {precio}")


SistemaDeVentaDeTickets.agregar_tipo_ticket("General", 15.2)
SistemaDeVentaDeTickets.agregar_tipo_ticket("VIP", 30.0)
SistemaDeVentaDeTickets.agregar_tipo_ticket("Estudiante", 9.0)

SistemaDeVentaDeTickets.registrar_venta("General", 6)
SistemaDeVentaDeTickets.registrar_venta("VIP", 3)
SistemaDeVentaDeTickets.registrar_venta("Estudiante", 4)

total_ingreso = SistemaDeVentaDeTickets.calcular_ingresos_totales()

#ingresos totales
print(f"Ingresos Totales: {total_ingreso:.2f}")

#precios de tickets
SistemaDeVentaDeTickets.mostrar_precios_tickets()
