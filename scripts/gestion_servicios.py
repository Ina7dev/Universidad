import tkinter as tk  # Importa el módulo tkinter para la interfaz gráfica
from tkinter import ttk, messagebox  # Importa widgets avanzados y cuadros de mensaje
import json  # Para trabajar con archivos JSON
import os  # Para operaciones del sistema de archivos
import re  # Añadir para validación de horario

# Nombre del archivo donde se almacenan los servicios
ARCHIVO_SERVICIOS = "servicios.json"

def cargar_servicios():
    """
    Carga los servicios desde el archivo JSON.
    Si el archivo no existe, retorna un diccionario vacío.
    """
    if os.path.exists(ARCHIVO_SERVICIOS):
        with open(ARCHIVO_SERVICIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_servicios(data):
    """
    Guarda el diccionario de servicios en el archivo JSON.
    """
    with open(ARCHIVO_SERVICIOS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def error_response(msg):
    """
    Muestra un mensaje de error al usuario.
    """
    messagebox.showwarning("Error", msg)

def validar_precio(precio):
    """
    Valida que el precio ingresado sea un número entero positivo y esté dentro de un rango razonable.
    """
    if not precio.isdigit():
        error_response("El precio debe ser un número entero.")
        return False
    precio_val = int(precio)
    if precio_val < 0:
        error_response("El precio no puede ser negativo.")
        return False
    if precio_val > 99999:
        error_response("El precio no puede superar 99.999.")
        return False
    return True

def validar_personas(personas):
    """
    Valida que la cantidad de personas ingresada sea un número entero positivo y esté dentro de un rango razonable.
    """
    if not personas.isdigit():
        error_response("La cantidad de personas debe ser un número entero.")
        return False
    cantidad = int(personas)
    if cantidad < 0:
        error_response("La cantidad no puede ser negativa.")
        return False
    if cantidad > 1000000:
        error_response("La cantidad es excesivamente alta.")
        return False
    return True

def validar_horario(horario):
    """
    Valida que el horario esté en formato HH:MM-HH:MM, 24 horas, minutos 0-59, horas 0-23, y rango válido.
    """
    if not isinstance(horario, str):
        error_response("El horario debe ser texto.")
        return False
    patron = r"^([01]?\d|2[0-3]):([0-5]\d)-([01]?\d|2[0-3]):([0-5]\d)$"
    match = re.match(patron, horario)
    if not match:
        error_response("El horario debe tener formato HH:MM-HH:MM (24h). Ejemplo: 09:00-18:30")
        return False
    h1, m1, h2, m2 = map(int, match.groups())
    if (h1, m1) >= (h2, m2):
        error_response("La hora de inicio debe ser menor que la de fin.")
        return False
    return True

class ventanaCRUDservicios:
    """
    Clase para la ventana de gestión CRUD de servicios adicionales.
    Permite agregar, editar y eliminar servicios como Yoga, Spa, Tour, etc.
    """
    def __init__(self, on_close=None):
        # Carga los servicios existentes
        self.servicios = cargar_servicios()
        self.on_close = on_close
        # Crea una nueva ventana secundaria
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Servicios Adicionales")
        self.ventana.geometry("800x400")
        self.ventana.protocol("WM_DELETE_WINDOW", self._on_close)
        self.ventana.bind("<Escape>", lambda e: self.ventana.destroy())

        # Crea el Treeview para mostrar los servicios en forma de tabla
        self.tree = ttk.Treeview(
            self.ventana,
            columns=("ID", "Nombre", "Horario", "Precio", "Personas", "Límite"),
            show="headings"
        )
        # Define los encabezados de la tabla
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre Servicio")
        self.tree.heading("Horario", text="Horario")
        self.tree.heading("Precio", text="Precio ($CLP)")
        self.tree.heading("Personas", text="Cantidad Personas")
        self.tree.heading("Límite", text="¿Tiene Límite?")
        self.tree.pack(pady=10, fill="both", expand=True)

        # Actualiza la tabla con los servicios cargados
        self.actualizar_tabla()

        # Frame para los botones de acción (Agregar, Editar, Eliminar)
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        # Botón para agregar un nuevo servicio
        tk.Button(frame_botones, text="Agregar", command=self.agregar_servicio).grid(row=0, column=0, padx=5)
        # Botón para editar el servicio seleccionado
        tk.Button(frame_botones, text="Editar", command=self.editar_servicio).grid(row=0, column=1, padx=5)
        # Botón para eliminar el servicio seleccionado
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_servicio).grid(row=0, column=2, padx=5)

    def _on_close(self):
        self.ventana.destroy()
        if self.on_close:
            self.on_close()

    def actualizar_tabla(self):
        """
        Actualiza el Treeview con los servicios actuales.
        Borra la tabla y la vuelve a llenar con los datos actualizados.
        """
        self.tree.delete(*self.tree.get_children())
        for id_serv, data in self.servicios.items():
            self.tree.insert(
                "", "end",
                values=(
                    id_serv,
                    data["nombre"],
                    data["horario"],
                    data["precio"],
                    data["personas"],
                    data["limite"]
                )
            )

    def agregar_servicio(self):
        """
        Abre el formulario para agregar un nuevo servicio.
        """
        self.ventana_formulario("Agregar Servicio")

    def editar_servicio(self):
        """
        Abre el formulario para editar el servicio seleccionado en la tabla.
        """
        seleccion = self.tree.selection()
        if seleccion:
            id_serv = self.tree.item(seleccion[0])["values"][0]
            self.ventana_formulario("Editar Servicio", id_serv)

    def eliminar_servicio(self):
        """
        Elimina el servicio seleccionado tras confirmación del usuario.
        """
        seleccion = self.tree.selection()
        if seleccion:
            id_serv = self.tree.item(seleccion[0])["values"][0]
            id_serv_str = str(id_serv)  # Asegura que sea string
            if messagebox.askyesno("Confirmar", f"¿Seguro que desea borrar el servicio '{id_serv_str}'?"):
                if id_serv_str in self.servicios:
                    self.servicios.pop(id_serv_str)
                    guardar_servicios(self.servicios)
                    self.actualizar_tabla()
                else:
                    error_response(f"No se encontró el servicio con ID '{id_serv_str}'.")

    def ventana_formulario(self, titulo, id_servicio=None):
        """
        Abre una ventana secundaria con el formulario para agregar o editar un servicio.
        Si se pasa un id_servicio, se cargan los datos existentes para editar.
        """
        ventana = tk.Toplevel(self.ventana)
        ventana.title(titulo)

        # Obtiene los datos del servicio si es edición
        servicio = self.servicios.get(id_servicio, {})

        # Campo para el ID del servicio
        tk.Label(ventana, text="ID:").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack()
        if id_servicio:
            id_entry.insert(0, id_servicio)
            id_entry.config(state="disabled")  # No permite modificar el ID al editar

        # Campo para el nombre del servicio
        tk.Label(ventana, text="Nombre del Servicio:").pack()
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack()
        nombre_entry.insert(0, servicio.get("nombre", ""))

        # Campo para el horario del servicio
        tk.Label(ventana, text="Horario (ej: 10:00-12:00):").pack()
        horario_entry = tk.Entry(ventana)
        horario_entry.pack()
        horario_entry.insert(0, servicio.get("horario", ""))

        # Campo para el precio del servicio
        tk.Label(ventana, text="Precio ($CLP):").pack()
        precio_entry = tk.Entry(ventana)
        precio_entry.pack()
        precio_entry.insert(0, servicio.get("precio", ""))

        # Campo para la cantidad de personas
        tk.Label(ventana, text="Cantidad de Personas:").pack()
        personas_entry = tk.Entry(ventana)
        personas_entry.pack()
        personas_entry.insert(0, servicio.get("personas", ""))

        # Campo para indicar si tiene límite de personas
        tk.Label(ventana, text="¿Tiene límite de personas? (Sí/No):").pack()
        limite_entry = tk.Entry(ventana)
        limite_entry.pack()
        limite_entry.insert(0, servicio.get("limite", ""))

        def guardar():
            """
            Valida y guarda los datos ingresados en el formulario.
            Si es válido, actualiza el diccionario y el archivo JSON.
            """
            id_val = id_servicio if id_servicio else id_entry.get().strip()
            nombre = nombre_entry.get().strip()
            horario = horario_entry.get().strip()
            precio = precio_entry.get().strip()
            personas = personas_entry.get().strip()
            limite = limite_entry.get().strip().capitalize() or "No"

            if not id_val:
                return error_response("El ID del servicio es obligatorio.")
            if not nombre:
                return error_response("El nombre del servicio es obligatorio.")
            if not horario:
                return error_response("El horario es obligatorio.")
            if not validar_horario(horario):
                return
            if not validar_precio(precio):
                return
            if not validar_personas(personas):
                return
            if limite not in ["Sí", "No", "Si", "No"]:
                return error_response("El campo límite debe ser 'Sí' o 'No'.")

            nuevo = {
                "nombre": nombre,
                "horario": horario,
                "precio": precio,
                "personas": personas,
                "limite": "Sí" if limite in ["Sí", "Si"] else "No"
            }
            self.servicios[id_val] = nuevo
            guardar_servicios(self.servicios)
            self.actualizar_tabla()
            ventana.destroy()

        # Botón para guardar los datos del formulario
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)