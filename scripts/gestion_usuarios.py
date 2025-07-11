from .users import User
from .gestion_clientes import ventanaCRUDclientes, ventanaCliente
from .gestion_rol import ventanaCRUDroles, cargarRoles
from .gestion_reservas import ventanaCRUDreservas
from .gestion_habitaciones import GestionHabitaciones
from .gestion_servicios import ventanaCRUDservicios
from .gestion_feedback import ventanaCRUDfeedback, ventanaFeedbackCliente
from .gestion_mantenimiento import ventanaCRUDMantenimiento
from .crearespacioevento import cargar_espacios, guardar_espacios
from .reservaevento import cargar_datos, guardar_reservas as guardar_reservas_evento
from .gestion_usuarios2 import ventanaRecepcionista

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os
import re
from datetime import datetime, timedelta

class gestionRecepcionistas:
    def __init__(self):
        self.archivo = "recepcionistas.json"

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                return json.load(f)
        return {}

    def guardar(self, data):
        with open(self.archivo, 'w') as f:
            json.dump(data, f, indent=4)

class gestionUsuarios:
    def __init__(self):
        self.archivo = "usuarios.json"

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                return json.load(f)
        return {}

    def guardar(self, data):
        with open(self.archivo, 'w') as f:
            json.dump(data, f, indent=4)

def verificacion(text):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(regex, text)

def buscar_correo(correo, dict):
    for data in dict.values():
        if correo == data.get("email"):
            return True
    return False

class ventanaRegistro:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.window = tk.Toplevel()
        self.window.title("Registrarse")
        self.window.geometry("350x300")
        self.window.resizable(False, False)
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (350 // 2)
        y = (self.window.winfo_screenheight() // 2) - (300 // 2)
        self.window.geometry(f"+{x}+{y}")

        frame = ttk.Frame(self.window, style="Login.TFrame", width=340, height=290)
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(False)

        for i in range(6):
            frame.rowconfigure(i, weight=1)
        for j in range(1):
            frame.columnconfigure(j, weight=1)

        ttk.Label(frame, text="Registro de Usuario", style="Login.TLabel", font=("Arial", 15, "bold")).grid(row=0, column=0, pady=10, sticky="nsew")
        ttk.Label(frame, text="Nombre completo:", style="Login.TLabel").grid(row=1, column=0, pady=3, sticky="nsew")
        self.nombre_entry = ttk.Entry(frame)
        self.nombre_entry.grid(row=2, column=0, pady=3, sticky="nsew")
        
        ttk.Label(frame, text="Correo:", style="Login.TLabel").grid(row=3, column=0, pady=3, sticky="nsew")
        self.correo_entry = ttk.Entry(frame)
        self.correo_entry.grid(row=4, column=0, pady=3, sticky="nsew")

        ttk.Label(frame, text="Contraseña:", style="Login.TLabel").grid(row=5, column=0, pady=3, sticky="nsew")
        self.contra_entry = ttk.Entry(frame, show="*")
        self.contra_entry.grid(row=6, column=0, pady=3, sticky="nsew")

        ttk.Button(frame, text="Aceptar", command=self.guardar, style="Login.TButton").grid(row=7, column=0, pady=10, sticky="nsew")

    def guardar(self): 
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get().strip()
        contra = self.contra_entry.get().strip()
        usuarios = self.user_manager.cargar()

        if buscar_correo(correo, usuarios):
            messagebox.showwarning("Error", "Este correo ya está registrado.")
        else:
            if not verificacion(correo):
                messagebox.showwarning("Error", "Correo invalido")
            else:
                if len(contra) < 7: 
                    messagebox.showwarning("Error", "contraseña invalida")
                elif correo and contra:
                    user = User(name=nombre, email=correo, password=contra)
                    usuarios[user.name] = user.get_user()
                    self.user_manager.guardar(usuarios)
                    try:
                        with open("clientes.json", "r") as f:
                            clientes=json.load(f)
                    except FileNotFoundError:
                        clientes={}

                    clientes[correo]={
                        "nombre": nombre,
                        "correo": correo,
                        "telefono": "No asignado"
                    }

                    with open("clientes.json", "w") as f:
                        json.dump(clientes, f, indent=4)
                    messagebox.showinfo("Éxito", "Cuenta creada exitosamente.")
                    self.window.destroy()
                else:
                    messagebox.showwarning("Campos vacíos", "Completa todos los campos.")

class ventanaCRUDrecepcionistas:
    def __init__(self, recepcionista_manager):
        self.recepcionista_manager = recepcionista_manager
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Recepcionistas")
        self.ventana.geometry("800x500")
        self.recepcionistas = self.recepcionista_manager.cargar()

        self.tree = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Email"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Email", text="Email")
        self.tree.pack(pady=10, fill='both', expand=True)

        self.actualizar_tabla()

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_recepcionista).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Editar", command=self.editar_recepcionista).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_recepcionista).grid(row=0, column=2, padx=5)

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        for id_recep, data in self.recepcionistas.items():
            self.tree.insert("", "end", values=(id_recep, data["nombre"], data["email"]))

    def agregar_recepcionista(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar Recepcionista")

        tk.Label(ventana, text="ID:").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack()

        tk.Label(ventana, text="Nombre:").pack()
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack()

        tk.Label(ventana, text="Email:").pack()
        email_entry = tk.Entry(ventana)
        email_entry.pack()


        def guardar_nuevo():
            id_recep = id_entry.get().strip()
            if not verificacion(email_entry.get().strip()):
                messagebox.showwarning("Error", "Correo inválido")
                return
            nombre = nombre_entry.get().strip()
            email = email_entry.get().strip()

            
            if id_recep and nombre and email:
                if id_recep in self.recepcionistas:
                    messagebox.showwarning("Error", "Este ID ya está registrado")
                else:
                    self.recepcionistas[id_recep] = {
                        "nombre": nombre,
                        "email": email,
                    }
                    self.recepcionista_manager.guardar(self.recepcionistas)
                    self.actualizar_tabla()
                    ventana.destroy()
            else:
                messagebox.showwarning("Error", "Todos los campos son obligatorios")

        tk.Button(ventana, text="Guardar", command=guardar_nuevo).pack(pady=5)

    def eliminar_recepcionista(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_recep = self.tree.item(seleccion[0])['values'][0]
            if messagebox.askyesno("Confirmar", f"¿Eliminar al recepcionista {id_recep}?"):
                del self.recepcionistas[id_recep]
                self.recepcionista_manager.guardar(self.recepcionistas)
                self.actualizar_tabla()

    def editar_recepcionista(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_recep = self.tree.item(seleccion[0])['values'][0]
            datos = self.recepcionistas[id_recep]

            ventana = tk.Toplevel(self.ventana)
            ventana.title("Editar Recepcionista")

            tk.Label(ventana, text=f"ID: {id_recep}").pack()
            
            tk.Label(ventana, text="Nombre:").pack()
            nombre_entry = tk.Entry(ventana)
            nombre_entry.insert(0, datos["nombre"])
            nombre_entry.pack()

            tk.Label(ventana, text="Email:").pack()
            email_entry = tk.Entry(ventana)
            email_entry.insert(0, datos["email"])
            email_entry.pack()



            def guardar_edicion():
                nuevo_nombre = nombre_entry.get().strip()
                nuevo_email = email_entry.get().strip()
                if not verificacion(nuevo_email):
                    messagebox.showwarning("Error", "Correo inválido")
                    return
                nuevo_email = email_entry.get().strip()

                
                if nuevo_nombre and nuevo_email:
                    self.recepcionistas[id_recep] = {
                        "nombre": nuevo_nombre,
                        "email": nuevo_email,
                    }
                    self.recepcionista_manager.guardar(self.recepcionistas)
                    self.actualizar_tabla()
                    ventana.destroy()
                else:
                    messagebox.showwarning("Error", "Todos los campos son obligatorios")

            tk.Button(ventana, text="Guardar Cambios", command=guardar_edicion).pack(pady=5)

    

class ventanaCRUDusuarios:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Usuarios")
        self.ventana.geometry("800x400")
        self.usuarios = self.user_manager.cargar()

        self.tree = ttk.Treeview(self.ventana, columns=("Nombre" ,"Correo", "Contraseña", "Rol"), show='headings')
        
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Contraseña", text="Contraseña")
        self.tree.heading("Rol", text="Rol")
        self.tree.pack(pady=10, fill='both', expand=True)

        self.actualizar_tabla()

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_usuario).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Editar", command=self.editar_usuario).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_usuario).grid(row=0, column=2, padx=5)

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        for nombre, data in self.usuarios.items():
            self.tree.insert("", "end", values=(nombre, data["email"] , data["password"], data["rol"]))

    def agregar_usuario(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar Usuario")


        tk.Label(ventana, text="Nombre:").pack()
        Nombre_entry = tk.Entry(ventana)
        Nombre_entry.pack()

        tk.Label(ventana, text="Correo:").pack()
        correo_entry = tk.Entry(ventana)
        correo_entry.pack()

        tk.Label(ventana, text="Contraseña:").pack()
        contra_entry = tk.Entry(ventana)
        contra_entry.pack()

        tk.Label(ventana, text="Rol:").pack()
        rol_combobox = ttk.Combobox(ventana, values=[rol for rol in cargarRoles().keys()])
        rol_combobox.set("usuario")
        rol_combobox.pack()

        def guardar_nuevo():

            Nombre = Nombre_entry.get()
            correo = correo_entry.get().strip()
            contra = contra_entry.get().strip()
            rol = rol_combobox.get()
            
            if not verificacion(correo):
                messagebox.showwarning("Error", "Correo inválido")
                return
            if len(contra)< 7:
                messagebox.showwarning("Error", "Contraseña inválida")
                return
            if correo and contra and rol and Nombre:
                self.usuarios[Nombre] = {"email": correo , "password": contra, "rol": rol}
                self.user_manager.guardar(self.usuarios)
                self.actualizar_tabla()
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_nuevo).pack(pady=5)

    def eliminar_usuario(self):
        seleccion = self.tree.selection()
        if seleccion:
            correo = self.tree.item(seleccion[0])['values'][0]
            if messagebox.askyesno("Confirmar", f"¿Eliminar a {correo}?"):
                del self.usuarios[correo]
                self.user_manager.guardar(self.usuarios)
                self.actualizar_tabla()

    def editar_usuario(self):
        seleccion = self.tree.selection()
        if seleccion:
            Nombre = self.tree.item(seleccion[0])['values'][0]
            datos = self.usuarios[Nombre]

            ventana = tk.Toplevel(self.ventana)
            ventana.title("Editar Usuario")

            tk.Label(ventana, text=f"Nombre: {Nombre}").pack()
            

            tk.Label(ventana, text="Nueva Contraseña:").pack()
            contra_entry = tk.Entry(ventana)
            contra_entry.insert(0, datos["password"])
            contra_entry.pack()

            tk.Label(ventana, text="Rol:").pack()
            rol_combobox = ttk.Combobox(ventana, values=[rol for rol in cargarRoles().keys()])
            rol_combobox.set(datos["rol"])
            rol_combobox.pack()

            def guardar_edicion():
                nueva_contra = contra_entry.get()
                if not verificacion(datos["email"]):
                    messagebox.showwarning("Error", "Correo inválido")
                    return
                if len(nueva_contra) < 7:
                    messagebox.showwarning("Error", "Contraseña inválida")
                    return
                nuevo_rol = rol_combobox.get()
                self.usuarios[Nombre] = {"email": datos["email"] ,"password": nueva_contra , "rol": nuevo_rol}
                self.user_manager.guardar(self.usuarios)
                self.actualizar_tabla()
                ventana.destroy()

            tk.Button(ventana, text="Guardar Cambios", command=guardar_edicion).pack(pady=5)
    
class GestionEventos(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gestión de Espacios para Eventos")
        self.geometry("900x600")
        self.resizable(False, False)

        self.espacios = cargar_espacios()
        self.reservas = cargar_datos("reservas_eventos.json")

        self.tabs = ttk.Notebook(self)
        self.tab_espacios = tk.Frame(self.tabs)
        self.tab_reservas = tk.Frame(self.tabs)
        self.tabs.add(self.tab_espacios, text="Espacios")
        self.tabs.add(self.tab_reservas, text="Reservas")
        self.tabs.pack(fill="both", expand=True)

        self._crear_tab_espacios()
        self._crear_tab_reservas()

    def _crear_tab_espacios(self):
        # Treeview
        columnas = ("id", "nombre", "tipo", "capacidad", "ubicacion")
        self.tree_espacios = ttk.Treeview(self.tab_espacios, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tree_espacios.heading(col, text=col.capitalize())
            self.tree_espacios.column(col, width=150, anchor="center")
        self.tree_espacios.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self._mostrar_espacios()

        # Botones
        btn_frame = tk.Frame(self.tab_espacios)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Agregar", command=self._agregar_espacio).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Editar", command=self._editar_espacio).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self._eliminar_espacio).pack(side=tk.LEFT, padx=5)

    def _mostrar_espacios(self):
        self.tree_espacios.delete(*self.tree_espacios.get_children())
        for espacio in self.espacios:
            self.tree_espacios.insert("", "end", values=(
                espacio["id"],
                espacio["nombre"],
                espacio["tipo"],
                espacio["capacidad"],
                espacio["ubicacion"]
            ))

    def _agregar_espacio(self):
        def guardar():
            datos = {
                "id": entry_id.get().strip(),
                "nombre": entry_nombre.get().strip(),
                "tipo": entry_tipo.get().strip(),
                "capacidad": entry_capacidad.get().strip(),
                "ubicacion": entry_ubicacion.get().strip()
            }
            if not all(datos.values()):
                messagebox.showwarning("Error", "Todos los campos son obligatorios")
                return
            if not datos["capacidad"].isdigit() or int(datos["capacidad"]) <= 0:
                messagebox.showwarning("Error", "Capacidad debe ser un número positivo")
                return
            if any(e["id"] == datos["id"] for e in self.espacios):
                messagebox.showwarning("Error", "ID de espacio ya existe")
                return
            datos["capacidad"] = int(datos["capacidad"])
            self.espacios.append(datos)
            guardar_espacios(self.espacios)
            self._mostrar_espacios()
            ventana.destroy()
            messagebox.showinfo("Éxito", "Espacio agregado correctamente")

        ventana = tk.Toplevel(self.tab_espacios)
        ventana.title("Agregar Espacio")
        tk.Label(ventana, text="ID Espacio:").pack()
        entry_id = tk.Entry(ventana)
        entry_id.pack()
        tk.Label(ventana, text="Nombre:").pack()
        entry_nombre = tk.Entry(ventana)
        entry_nombre.pack()
        tk.Label(ventana, text="Tipo (Abierto/Cerrado):").pack()
        entry_tipo = tk.Entry(ventana)
        entry_tipo.pack()
        tk.Label(ventana, text="Capacidad:").pack()
        entry_capacidad = tk.Entry(ventana)
        entry_capacidad.pack()
        tk.Label(ventana, text="Ubicación:").pack()
        entry_ubicacion = tk.Entry(ventana)
        entry_ubicacion.pack()
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    def _editar_espacio(self):
        seleccionado = self.tree_espacios.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un espacio")
            return
        item = seleccionado[0]
        valores = self.tree_espacios.item(item, "values")
        espacio_id = valores[0]
        espacio = next((e for e in self.espacios if e["id"] == espacio_id), None)
        if not espacio:
            return

        ventana = tk.Toplevel(self.tab_espacios)
        ventana.title("Editar Espacio")
        tk.Label(ventana, text="Nombre:").pack()
        entry_nombre = tk.Entry(ventana)
        entry_nombre.insert(0, espacio["nombre"])
        entry_nombre.pack()
        tk.Label(ventana, text="Tipo:").pack()
        entry_tipo = tk.Entry(ventana)
        entry_tipo.insert(0, espacio["tipo"])
        entry_tipo.pack()
        tk.Label(ventana, text="Capacidad:").pack()
        entry_capacidad = tk.Entry(ventana)
        entry_capacidad.insert(0, str(espacio["capacidad"]))
        entry_capacidad.pack()
        tk.Label(ventana, text="Ubicación:").pack()
        entry_ubicacion = tk.Entry(ventana)
        entry_ubicacion.insert(0, espacio["ubicacion"])
        entry_ubicacion.pack()

        def guardar():
            nuevos_datos = {
                "nombre": entry_nombre.get().strip(),
                "tipo": entry_tipo.get().strip(),
                "capacidad": entry_capacidad.get().strip(),
                "ubicacion": entry_ubicacion.get().strip()
            }
            if not all(nuevos_datos.values()):
                messagebox.showwarning("Error", "Todos los campos son obligatorios")
                return
            if not nuevos_datos["capacidad"].isdigit() or int(nuevos_datos["capacidad"]) <= 0:
                messagebox.showwarning("Error", "Capacidad debe ser un número positivo")
                return
            espacio.update({
                "nombre": nuevos_datos["nombre"],
                "tipo": nuevos_datos["tipo"],
                "capacidad": int(nuevos_datos["capacidad"]),
                "ubicacion": nuevos_datos["ubicacion"]
            })
            guardar_espacios(self.espacios)
            self._mostrar_espacios()
            ventana.destroy()
            messagebox.showinfo("Éxito", "Espacio actualizado")

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    def _eliminar_espacio(self):
        seleccionado = self.tree_espacios.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un espacio")
            return
        item = seleccionado[0]
        valores = self.tree_espacios.item(item, "values")
        espacio_id = valores[0]
        if messagebox.askyesno("Confirmar", f"¿Eliminar espacio {espacio_id}?"):
            self.espacios = [e for e in self.espacios if e["id"] != espacio_id]
            guardar_espacios(self.espacios)
            self._mostrar_espacios()
            messagebox.showinfo("Éxito", "Espacio eliminado")

    def _crear_tab_reservas(self):
        # Treeview
        columnas = ("id_espacio", "nombre_evento", "fecha", "personas", "contacto")
        self.tree_reservas = ttk.Treeview(self.tab_reservas, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tree_reservas.heading(col, text=col.capitalize().replace("_", " "))
            self.tree_reservas.column(col, width=120, anchor="center")
        self.tree_reservas.pack(pady=10, fill=tk.BOTH, expand=True)
        self._mostrar_reservas()

        btn_frame = tk.Frame(self.tab_reservas)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Agregar", command=self._agregar_reserva).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self._eliminar_reserva).pack(side=tk.LEFT, padx=5)

    def _mostrar_reservas(self):
        self.tree_reservas.delete(*self.tree_reservas.get_children())
        for reserva in self.reservas:
            self.tree_reservas.insert("", "end", values=(
                reserva["id_espacio"],
                reserva["nombre_evento"],
                reserva["fecha"],
                reserva["personas"],
                reserva["contacto"]
            ))

    def _agregar_reserva(self):
        ventana = tk.Toplevel(self.tab_reservas)
        ventana.title("Agregar Reserva de Evento")

        tk.Label(ventana, text="Espacio:").pack()
        espacios_ids = [e["id"] for e in self.espacios]
        combo_espacio = ttk.Combobox(ventana, values=espacios_ids, state="readonly")
        combo_espacio.pack()
        if espacios_ids:
            combo_espacio.current(0)

        tk.Label(ventana, text="Nombre Evento:").pack()
        entry_nombre = tk.Entry(ventana)
        entry_nombre.pack()

        tk.Label(ventana, text="Fecha (DD-MM-YYYY):").pack()
        entry_fecha = tk.Entry(ventana)
        entry_fecha.pack()

        tk.Label(ventana, text="N° Personas:").pack()
        entry_personas = tk.Entry(ventana)
        entry_personas.pack()

        tk.Label(ventana, text="Contacto:").pack()
        entry_contacto = tk.Entry(ventana)
        entry_contacto.pack()

        def guardar():
            datos = {
                "id_espacio": combo_espacio.get(),
                "nombre_evento": entry_nombre.get().strip(),
                "fecha": entry_fecha.get().strip(),
                "personas": entry_personas.get().strip(),
                "contacto": entry_contacto.get().strip()
            }
            if not all(datos.values()):
                messagebox.showwarning("Error", "Todos los campos son obligatorios")
                return
            if not datos["personas"].isdigit() or int(datos["personas"]) <= 0:
                messagebox.showwarning("Error", "Número de personas inválido")
                return
            # Validar fecha (mínimo 2 semanas, formato DD-MM-YYYY)
            try:
                fecha_reserva = datetime.strptime(datos["fecha"], "%d-%m-%Y")
            except ValueError:
                messagebox.showwarning("Error", "Formato de fecha debe ser DD-MM-YYYY")
                return
            if fecha_reserva < datetime.now() + timedelta(days=14):
                messagebox.showwarning("Error", "Reserva debe tener al menos 2 semanas de anticipación")
                return
            espacio = next((e for e in self.espacios if e["id"] == datos["id_espacio"]), None)
            if not espacio:
                messagebox.showwarning("Error", "Espacio no encontrado")
                return
            if int(datos["personas"]) > espacio["capacidad"]:
                messagebox.showwarning("Error", f"Capacidad excedida (Máx: {espacio['capacidad']})")
                return
            if any(r for r in self.reservas if r["id_espacio"] == datos["id_espacio"] and r["fecha"] == datos["fecha"]):
                messagebox.showwarning("Error", "Espacio ya reservado para esa fecha")
                return
            datos["personas"] = int(datos["personas"])
            self.reservas.append(datos)
            guardar_reservas_evento(self.reservas)
            self._mostrar_reservas()
            ventana.destroy()
            messagebox.showinfo("Éxito", "Reserva creada correctamente")

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    def _eliminar_reserva(self):
        seleccionado = self.tree_reservas.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione una reserva")
            return
        item = seleccionado[0]
        valores = self.tree_reservas.item(item, "values")
        if messagebox.askyesno("Confirmar", "¿Cancelar esta reserva?"):
            self.reservas = [r for r in self.reservas if not (
                r["id_espacio"] == valores[0] and
                r["fecha"] == valores[2]
            )]
            guardar_reservas_evento(self.reservas)
            self._mostrar_reservas()
            messagebox.showinfo("Éxito", "Reserva cancelada")

class ventanaAcceso:
    def __init__(self, parent, on_all_closed=None):
        self.parent = parent
        self.user_manager = gestionUsuarios()
        self.recepcionista_manager = gestionRecepcionistas()
        self.on_all_closed = on_all_closed

        self.frame = ttk.Frame(parent, width=400, height=400)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.grid_propagate(False)

        for i in range(8):
            self.frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.frame.columnconfigure(j, weight=1)

        ttk.Label(self.frame, text="Inicio", font=("Arial", 18, "bold")).grid(column=0, row=0, columnspan=4, pady=10, sticky="nsew")
        ttk.Label(self.frame, text="Usuario").grid(column=0, row=1, columnspan=4, pady=10, sticky="nsew")
        self.user_entry = ttk.Entry(self.frame, width=30)
        self.user_entry.grid(row=2, column=1, pady=5, columnspan=2, sticky="nsew")
        self.user_entry.focus_set()
        self.user_entry.bind("<Return>", self._focus_pass_entry)

        ttk.Label(self.frame, text="Contraseña").grid(column=0, row=3, columnspan=4, pady=10, sticky="nsew")
        self.pass_entry = ttk.Entry(self.frame, width=30, show="*")
        self.pass_entry.grid(row=4, column=1, pady=5, sticky="nsew")
        self.pass_entry.bind("<Return>", self._login_event)

        self.show_password_var = tk.BooleanVar(value=False)
        def toggle_password():
            self.pass_entry.config(show="" if self.show_password_var.get() else "*")
        show_pass_cb = ttk.Checkbutton(
            self.frame, variable=self.show_password_var, command=toggle_password, width=2
        )
        show_pass_cb.grid(row=4, column=2, padx=2, sticky="w")
        ttk.Label(self.frame, text="Mostrar").grid(row=4, column=3, sticky="w")

        ttk.Button(self.frame, text="Aceptar", command=self.verificar).grid(column=0, row=5, columnspan=4, pady=8, sticky="nsew")
        ttk.Button(self.frame, text="Registrarse", command=lambda: ventanaRegistro(self.user_manager)).grid(column=0, row=6, columnspan=4, pady=4, sticky="nsew")
        ttk.Button(self.frame, text="Iniciar como Cliente (Demo)", command=self._demo_cliente).grid(column=0, row=7, columnspan=4, pady=4, sticky="nsew")

    def _focus_pass_entry(self, event):
        self.pass_entry.focus_set()

    def _login_event(self, event):
        self.verificar()

    def _demo_cliente(self):
        usuarios = self.user_manager.cargar()
        demo_user = None
        for name, dato in usuarios.items():
            if dato.get("rol") == "usuario":
                demo_user = dato
                break
        if not demo_user:
            demo_user = {"email": "demo_cliente@hotel.com", "password": "demo", "rol": "usuario"}
        for widget in self.parent.winfo_children():
            widget.destroy()
        ventanaCliente(demo_user, on_close=self.on_all_closed)

    def verificar(self):
        usuarios = self.user_manager.cargar()
        email = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()
        login = False     
        logged_user = {}
        
        for name, dato in usuarios.items():
            if email == dato["email"]: 
                if password == dato["password"]:
                    logged_user = dato
                    login = True
                    break

        if login:
            messagebox.showinfo("Inicio de sesión correcto", f"Bienvenido {name}")
            for widget in self.parent.winfo_children():
                widget.destroy()
            def on_child_close():
                ventanas = [w for w in self.parent.winfo_toplevel().winfo_children() if isinstance(w, tk.Toplevel)]
                if not ventanas and self.on_all_closed:
                    self.on_all_closed()
            if logged_user.get("rol") == "admin":
                menu_admin = tk.Toplevel()
                menu_admin.title("Menú de Administrador")
                menu_admin.geometry("350x420")
                menu_admin.resizable(False, False)
                menu_admin.update_idletasks()
                x = (menu_admin.winfo_screenwidth() // 2) - (350 // 2)
                y = (menu_admin.winfo_screenheight() // 2) - (420 // 2)
                menu_admin.geometry(f"+{x}+{y}")
                menu_admin.protocol("WM_DELETE_WINDOW", lambda: [menu_admin.destroy(), on_child_close()])

                admin_frame = ttk.Frame(menu_admin, width=340, height=410)
                admin_frame.pack(expand=True, fill="both")
                admin_frame.grid_propagate(False)

                for i in range(10):
                    admin_frame.rowconfigure(i, weight=1)
                for j in range(1):
                    admin_frame.columnconfigure(j, weight=1)

                ttk.Label(admin_frame, text="Menú de Administrador", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=12, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Clientes",
                        command=lambda: ventanaCRUDclientes(on_close=on_child_close)).grid(row=1, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Usuarios", 
                        command=lambda: ventanaCRUDusuarios(self.user_manager)).grid(row=2, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Roles", 
                        command=lambda: ventanaCRUDroles()).grid(row=3, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Reservas", 
                        command=lambda: ventanaCRUDreservas(on_close=on_child_close)).grid(row=4, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Habitaciones", 
                        command=lambda: GestionHabitaciones(on_close=on_child_close)).grid(row=5, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Servicios",
                        command=lambda: ventanaCRUDservicios(on_close=on_child_close)).grid(row=6, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Feedback",
                        command=lambda: ventanaCRUDfeedback()).grid(row=7, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Mantenimiento / Incidencias",
                        command=lambda: ventanaCRUDMantenimiento()).grid(row=8, column=0, pady=6, sticky="nsew")
                ttk.Button(admin_frame, text="Gestión de Espacios para Eventos",
                        command=lambda: GestionEventos()).grid(row=9, column=0, pady=6, sticky="nsew")
            elif logged_user.get("rol") == "recepcionista":
                ventanaRecepcionista(self.parent)
            else:
                menu_usuario = tk.Toplevel()
                menu_usuario.title("Menú de Usuario")
                menu_usuario.geometry("350x260")
                menu_usuario.resizable(False, False)
                menu_usuario.update_idletasks()
                x = (menu_usuario.winfo_screenwidth() // 2) - (350 // 2)
                y = (menu_usuario.winfo_screenheight() // 2) - (260 // 2)
                menu_usuario.geometry(f"+{x}+{y}")
                menu_usuario.protocol("WM_DELETE_WINDOW", lambda: [menu_usuario.destroy(), on_child_close()])

                user_frame = ttk.Frame(menu_usuario, width=340, height=250)
                user_frame.pack(expand=True, fill="both")
                user_frame.grid_propagate(False)

                for i in range(4):
                    user_frame.rowconfigure(i, weight=1)
                for j in range(1):
                    user_frame.columnconfigure(j, weight=1)

                ttk.Label(user_frame, text="Menú de Usuario", font=("Arial", 15, "bold")).grid(row=0, column=0, pady=10, sticky="nsew")
                ttk.Button(user_frame, text="Mis Datos", command=lambda: ventanaCliente(logged_user, on_close=self.on_all_closed)).grid(row=1, column=0, pady=8, sticky="nsew")
                ttk.Button(user_frame, text="Mis Sugerencias y Reclamos", command=lambda: ventanaFeedbackCliente(logged_user)).grid(row=2, column=0, pady=8, sticky="nsew")
                ttk.Button(user_frame, text="Cerrar Sesión", command=lambda: [menu_usuario.destroy(), on_child_close()]).grid(row=3, column=0, pady=8, sticky="nsew")
        else:
            messagebox.showinfo("Inicio de sesión inválido", "Usuario o contraseña incorrectos")
