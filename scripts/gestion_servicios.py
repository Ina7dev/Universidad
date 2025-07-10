import tkinter as tk  # Importa el módulo tkinter para la interfaz gráfica
from tkinter import ttk, messagebox  # Importa widgets avanzados y cuadros de mensaje
import json  # Para trabajar con archivos JSON
import os  # Para operaciones del sistema de archivos

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

class ventanaCRUDservicios:
    """
    Clase para la ventana de gestión CRUD de servicios adicionales.
    Permite agregar, editar y eliminar servicios como Yoga, Spa, Tour, etc.
    """
    def __init__(self):
        estilo = ttk.Style()
        estilo.configure("Azul.TButton",
                        background="#add8e6",
                        foreground="#0d47a1",
                        font=("Arial", 12, "bold"),
                        padding=8,
                        borderwidth=1)
        estilo.map("Azul.TButton",
                  background=[("active", "#90caf9")])
        estilo.configure("Azul.TLabelframe",
                        background="#add8e6",
                        borderwidth=2,
                        relief="ridge")
        estilo.configure("Azul.TLabelframe.Label",
                        background="#add8e6",
                        foreground="#0d47a1",
                        font=("Arial", 12, "bold"))
        estilo.configure("Azul.TFrame",
                        background="#add8e6",
                        borderwidth=2,
                        relief="ridge")

        # Carga los servicios existentes
        self.servicios = cargar_servicios()
        # Crea una nueva ventana secundaria
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Servicios")
        menu_width = 950
        menu_height = 700
        self.ventana.geometry(f"{menu_width}x{menu_height}")
        self.ventana.update_idletasks()
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        x = (screen_width // 2) - (menu_width // 2)
        y = (screen_height // 2) - (menu_height // 2)
        self.ventana.geometry(f"{menu_width}x{menu_height}+{x}+{y}")
        self.ventana.configure(bg="#add8e6")

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
        tk.Button(frame_botones, text="Agregar", command=self.agregar_servicio, style="Azul.TButton").grid(row=0, column=0, padx=5)
        # Botón para editar el servicio seleccionado
        tk.Button(frame_botones, text="Editar", command=self.editar_servicio, style="Azul.TButton").grid(row=0, column=1, padx=5)
        # Botón para eliminar el servicio seleccionado
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_servicio, style="Azul.TButton").grid(row=0, column=2, padx=5)

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
            if messagebox.askyesno("Confirmar", f"¿Seguro que querís borrar el servicio '{id_serv}'?"):
                self.servicios.pop(id_serv)
                guardar_servicios(self.servicios)
                self.actualizar_tabla()

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
            nuevo = {
                "nombre": nombre_entry.get().strip(),
                "horario": horario_entry.get().strip(),
                "precio": precio_entry.get().strip(),
                "personas": personas_entry.get().strip(),
                "limite": limite_entry.get().strip().capitalize() or "No"
            }
            # Validaciones básicas
            if not id_val or not nuevo["nombre"]:
                messagebox.showwarning("Error", "El ID y el nombre son obligatorios, po.")
                return
            if not nuevo["precio"].isdigit():
                messagebox.showwarning("Error", "El precio tiene que ser un número, compadre.")
                return
            if not nuevo["personas"].isdigit():
                messagebox.showwarning("Error", "La cantidad de personas debe ser un número.")
                return
            # Guarda el servicio y actualiza la tabla
            self.servicios[id_val] = nuevo
            guardar_servicios(self.servicios)
            self.actualizar_tabla()
            ventana.destroy()

        # Botón para guardar los datos del formulario
        tk.Button(ventana, text="Guardar", command=guardar, style="Azul.TButton").pack(pady=10)