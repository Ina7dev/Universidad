import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import re
from .gestion_feedback import ventanaFeedbackCliente

ARCHIVO_CLIENTES = "clientes.json"
ARCHIVO_RESERVAS = "reservas.json"

def error_response(msg, parent=None):
    messagebox.showwarning("Error", msg, parent=parent)

class ventanaCliente:
    def __init__(self, datos_usuario, on_close=None):
        self.usuario = datos_usuario
        self.reservas = self.cargar_reservas()
        self.on_close = on_close

        self.ventana = tk.Toplevel()

        self.ventana.transient()      
        self.ventana.grab_set()          
        self.ventana.focus_set()          


        self.ventana.title("Panel del Cliente")
        self.ventana.geometry("500x400")
        self.ventana.protocol("WM_DELETE_WINDOW", self._on_close)

        frame = ttk.Frame(self.ventana, style="Login.TFrame", width=480, height=380)
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(False)
        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for j in range(1):
            frame.columnconfigure(j, weight=1)
        ttk.Label(frame, text=f"Bienvenido, {self.usuario['email']}", style="Login.TLabel", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=10, sticky="nsew")
        ttk.Button(frame, text="Ver mis datos", command=self.ver_datos, style="Login.TButton").grid(row=1, column=0, pady=10, sticky="nsew")
        ttk.Button(frame, text="Ver mis reservas", command=self.ver_reservas, style="Login.TButton").grid(row=2, column=0, pady=10, sticky="nsew")
        ttk.Button(frame, text="Mis Sugerencias y Reclamos", command=self._abrir_feedback, style="Login.TButton").grid(row=3, column=0, pady=10, sticky="nsew")
        ttk.Button(frame, text="Cerrar", command=self._on_close, style="Login.TButton").grid(row=4, column=0, pady=10, sticky="nsew")

    def _on_close(self):
        self.ventana.destroy()
        if self.on_close:
            self.on_close()

    def cargar_reservas(self):
        if os.path.exists("reservas.json"):
            with open("reservas.json", "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def ver_datos(self):
        info = f"Correo: {self.usuario['email']}\nContraseña: {self.usuario['password']}\nRol: {self.usuario['rol']}"
        messagebox.showinfo("Mis datos", info, parent=self.ventana)
    
    def ver_reservas(self):
        lista = [r for r in self.reservas.values() if r["cliente_id"] == self.usuario["email"]]

        if not lista:
            messagebox.showinfo("Reservas", "No tienes reservas registradas.", parent=self.ventana)
            return

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Mis Reservas")
        ventana.geometry("400x300")
        frame = ttk.Frame(ventana, style="Login.TFrame")
        frame.pack(expand=True, fill="both")
        for reserva in lista:
            texto = f"Habitación: {reserva['habitacion']}\nEntrada: {reserva['entrada']}\nSalida: {reserva['salida']}"
            ttk.Label(frame, text=texto, style="Login.TLabel", font=("Arial", 12, "bold")).pack(pady=5, fill="x")

    def _abrir_feedback(self):
        ventanaFeedbackCliente(self.usuario)

def cargar_clientes():
    if os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_clientes(data):
    with open(ARCHIVO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def cargar_reservas():
    if os.path.exists(ARCHIVO_RESERVAS):
        with open(ARCHIVO_RESERVAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def verificacion(correo):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(regex, correo)

def validar_telefono(telefono):
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def guardar_reservas(data):
    with open(ARCHIVO_RESERVAS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

class ventanaCRUDclientes:
    def __init__(self, on_close=None):
        self.clientes = cargar_clientes()
        self.reservas = cargar_reservas()
        self.on_close = on_close

        self.ventana = tk.Toplevel()

        self.ventana.transient()
        self.ventana.grab_set()
        self.ventana.focus_set()

        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("900x500")
        self.ventana.protocol("WM_DELETE_WINDOW", self._on_close)
        self.ventana.bind("<Escape>", lambda e: self.ventana.destroy())


        frame = ttk.Frame(self.ventana, style="Login.TFrame")
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(False)
        frame.config(borderwidth=4, relief="solid")

        search_frame = ttk.Frame(frame, style="Login.TFrame")
        search_frame.pack(pady=5)
        ttk.Label(search_frame, text="Buscar:", style="Login.TLabel", font=("Arial", 12, "bold")).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._filtrar_clientes)
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left")

        self.tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Correo", "Teléfono"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.pack(pady=10, fill="both", expand=True)

        self.actualizar_tabla()

        frame_botones = ttk.Frame(frame, style="Login.TFrame")
        frame_botones.pack(pady=10)
        ttk.Button(frame_botones, text="Agregar", command=self.agregar_cliente, style="Login.TButton").grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Editar", command=self.editar_cliente, style="Login.TButton").grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_cliente, style="Login.TButton").grid(row=0, column=2, padx=5)
        ttk.Button(frame_botones, text="Reservar", command=self.hacer_reserva, style="Login.TButton").grid(row=0, column=3, padx=5)

    def _on_close(self):
        self.ventana.destroy()
        if self.on_close:
            self.on_close()

    def _filtrar_clientes(self, *args):
        filtro = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        for cliente in self.clientes:
            nombre = cliente.get("Nombre", cliente.get("nombre", ""))
            correo = cliente.get("Correo", cliente.get("correo", ""))
            if filtro in nombre.lower() or filtro in correo.lower():
                id_cliente = cliente.get("N° habitación", "")
                telefono = cliente.get("Teléfono", cliente.get("telefono", ""))
                self.tree.insert("", "end", values=(id_cliente, nombre, correo, telefono))

    def actualizar_tabla(self):
        self._filtrar_clientes()

    def agregar_cliente(self):
        self.ventana_formulario("Agregar Cliente")

    def editar_cliente(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_cliente = self.tree.item(seleccion[0])["values"][0]
            self.ventana_formulario("Editar Cliente", id_cliente)

    def eliminar_cliente(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_cliente = self.tree.item(seleccion[0])["values"][0]
            idx = next((i for i, c in enumerate(self.clientes) if c.get("N° habitación", "") == id_cliente), None)
            if idx is None:
                messagebox.showerror("Error", f"No se encontró al cliente con ID '{id_cliente}'", parent=self.ventana)
                return
            if messagebox.askyesno("Confirmar", f"¿Eliminar al cliente {id_cliente}?", parent=self.ventana):
                self.clientes.pop(idx)
                guardar_clientes(self.clientes)
                self.actualizar_tabla()

    def ventana_formulario(self, titulo, id_cliente=None):
        ventana = tk.Toplevel(self.ventana)

        self.ventana.transient()
        self.ventana.grab_set()
        self.ventana.focus_set()

        ventana.title(titulo)
        ventana.bind("<Escape>", lambda e: ventana.destroy())

        form_frame = ttk.Frame(ventana, style="Login.TFrame")
        form_frame.pack(expand=True, fill="both")
        form_frame.grid_propagate(False)

        cliente = next((c for c in self.clientes if c.get("N° habitación", "") == id_cliente), {}) if id_cliente else {}

        ttk.Label(form_frame, text="ID:", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        id_entry = ttk.Entry(form_frame)
        id_entry.pack()
        if id_cliente:
            id_entry.insert(0, id_cliente)
            id_entry.config(state="disabled")

        ttk.Label(form_frame, text="Nombre:", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        nombre_entry = ttk.Entry(form_frame)
        nombre_entry.pack()
        nombre_entry.insert(0, cliente.get("Nombre", cliente.get("nombre", "")))

        ttk.Label(form_frame, text="Correo:", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        correo_entry = ttk.Entry(form_frame)
        correo_entry.pack()
        correo_entry.insert(0, cliente.get("Correo", cliente.get("correo", "")))

        ttk.Label(form_frame, text="Teléfono:", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        tel_entry = ttk.Entry(form_frame)
        tel_entry.pack()
        tel_entry.insert(0, cliente.get("Teléfono", cliente.get("telefono", "")))

        def guardar():
            id_val = id_cliente if id_cliente else id_entry.get().strip()
            nombre_val = nombre_entry.get().strip()
            correo_val = correo_entry.get().strip()
            tel_val = tel_entry.get().strip()
            if not id_val:
                return error_response("El campo 'ID' es obligatorio.", parent=self.ventana)
            if not nombre_val:
                return error_response("El campo 'Nombre' es obligatorio.", parent=self.ventana)
            if not correo_val:
                return error_response("El campo 'Correo' es obligatorio.", parent=self.ventana)
            if not verificacion(correo_val):
                return error_response("El correo electrónico no es válido.", parent=self.ventana)
            if tel_val and not validar_telefono(tel_val):
                return error_response("El teléfono debe contener solo números y tener entre 7 y 15 dígitos.", parent=self.ventana)
            nuevo = {
                "N° habitación": id_val,
                "Nombre": nombre_val,
                "Correo": correo_val,
                "Teléfono": tel_val
            }
            idx = next((i for i, c in enumerate(self.clientes) if c.get("N° habitación", "") == id_val), None)
            if idx is not None:
                self.clientes[idx] = nuevo
            else:
                self.clientes.append(nuevo)
            guardar_clientes(self.clientes)
            self.actualizar_tabla()
            ventana.destroy()

        ttk.Button(form_frame, text="Guardar", command=guardar, style="Login.TButton").pack(pady=10)

    def hacer_reserva(self):
        seleccion = self.tree.selection()
        if not seleccion:
            error_response("Debe seleccionar un cliente para realizar una reserva.")
            return

        id_cliente = self.tree.item(seleccion[0])["values"][0]
        correo_cliente = self.tree.item(seleccion[0])["values"][2]
        habitaciones = []
        if os.path.exists("habitaciones.json"):
            with open("habitaciones.json", "r", encoding="utf-8") as f:
                habitaciones_data = json.load(f)
                if isinstance(habitaciones_data, list):
                    habitaciones = [
                        f"{h['id']} | {h['tipo']} | {h['estado']}"
                        for h in habitaciones_data
                    ]

        ventana = tk.Toplevel(self.ventana)

        self.ventana.transient()
        self.ventana.grab_set()
        self.ventana.focus_set()

        ventana.title("Nueva Reserva")

        ttk.Label(ventana, text="Habitación:", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        habitacion_var = tk.StringVar()
        habitacion_combo = ttk.Combobox(ventana, textvariable=habitacion_var, values=habitaciones, state="readonly")
        habitacion_combo.pack()



        ttk.Label(ventana, text="Noches:", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        noches_entry = ttk.Entry(ventana)
        noches_entry.pack()


        ttk.Label(ventana, text="Personas:", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        personas_entry = ttk.Entry(ventana)
        personas_entry.pack()

        ttk.Label(ventana, text="Fecha entrada (DD-MM-YYYY):", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        entrada_entry = ttk.Entry(ventana)
        entrada_entry.pack()



        ttk.Label(ventana, text="Fecha salida (DD-MM-YYYY):", style="Login.TLabel", font=("Arial", 12, "bold")).pack()
        salida_entry = ttk.Entry(ventana)
        salida_entry.pack()

        def guardar_reserva():
            
            habitacion_info = habitacion_var.get().strip()
            
            entrada = entrada_entry.get().strip()
            
            salida = salida_entry.get().strip()
            noches = noches_entry.get().strip()
            personas = personas_entry.get().strip()
            if not noches.isdigit() or int(noches) <= 0:
                return error_response("El campo 'Noches' debe ser un número positivo.")
            if not personas.isdigit() or int(personas) <= 0:
                return error_response("El campo 'Personas' debe ser un número positivo.")
            if not habitacion_info:
                return error_response("El campo 'Habitación' es obligatorio.")
            if not entrada or not salida:
                return error_response("Debe ingresar las fechas de entrada y salida.")
            try:
                entrada_dt = datetime.strptime(entrada, "%d-%m-%Y")
                salida_dt = datetime.strptime(salida, "%d-%m-%Y")
            except ValueError:
                return error_response("El formato de fecha debe ser DD-MM-YYYY.")
            if entrada_dt >= salida_dt:
                return error_response("La fecha de entrada debe ser anterior a la fecha de salida.")
            habitacion_id = habitacion_info.split(" | ")[0]
            for r in self.reservas.values():
                if r["habitacion"] == habitacion_id:
                    r_entrada = datetime.strptime(r["entrada"], "%d-%m-%Y")
                    r_salida = datetime.strptime(r["salida"], "%d-%m-%Y")
                    if not (salida_dt <= r_entrada or entrada_dt >= r_salida):
                        return error_response("Ya existe una reserva para esa habitación en las fechas seleccionadas.")
            
            
            reserva = {
                "cliente_id": correo_cliente,
                "piso": habitacion_info[0] ,
                "tipo_habitacion": habitacion_info.split(" | ")[1],
                "personas": int(personas),
                "habitacion": habitacion_id,
                "entrada": entrada,
                "salida": salida,
                "noches": int(noches),
            }
            clave = f"{correo_cliente}"
            self.reservas[clave] = reserva
            guardar_reservas(self.reservas)
            messagebox.showinfo("Éxito", "Reserva guardada correctamente.")
            ventana.destroy()

        ttk.Button(ventana, text="Confirmar Reserva", command=guardar_reserva, style="Login.TButton").pack(pady=10)