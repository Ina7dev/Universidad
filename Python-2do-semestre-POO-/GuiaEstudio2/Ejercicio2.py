class Suscripcion:
    descuento_anual = 0.15
    descuento_bienvenida = 0.10

    def __init__(self, nombre_cliente, tipo_suscripcion, costo):
        self._nombre_cliente = nombre_cliente
        self._tipo_suscripcion = tipo_suscripcion
        self._costo = costo

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, costo):
        assert costo >= 0, "El costo no puede ser negativo."
        self._costo = costo

    def aplicar_descuento(self):
        if self._tipo_suscripcion == "anual":
            self._costo *= (1 - Suscripcion.descuento_anual)

    def mostrar_detalles(self):
        # Retornar los detalles en lugar de imprimir directamente
        return f"Cliente: {self._nombre_cliente}, Tipo: {self._tipo_suscripcion}, Costo: {self._costo}"

    @staticmethod
    def calcular_descuento_bienvenida(costo):
        return costo * (1 - Suscripcion.descuento_bienvenida)

suscripcion_cliente = Suscripcion("Ina Valentina", "anual", 1500)

#Detalles iniciales
detalle_normal = suscripcion_cliente.mostrar_detalles()
print(f"Detalle con precio normal: {detalle_normal}")

#descuento anual
suscripcion_cliente.aplicar_descuento()

#después de aplicar el descuento
detalle_anual = suscripcion_cliente.mostrar_detalles()
print(f"Detalle con descuento anual: {detalle_anual}")

#costo con descuento de bienvenida
costo_con_descuento = Suscripcion.calcular_descuento_bienvenida(1500)
print(f"Costo con descuento de bienvenida: {costo_con_descuento}")
