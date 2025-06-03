from users import User
from gestion_clientes import ventanaCRUDclientes, ventanaCliente
from gestion_rol import ventanaCRUDroles, cargarRoles
from gestion_reservas import ventanaCRUDreservas
from gestion_habitaciones import GestionHabitaciones
from gestion_servicios import ventanaCRUDservicios 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os
import re


class gestionRecepcionistas:
    def __init__(self):
        self.archivo = "recepcionistas.json"

    def cargar(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    return json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
        return {}

    def guardar(self, data):
        try:
            with open(self.archivo, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")

class gestionUsuarios:
    def __init__(self):
        self.archivo = "usuarios.json"

    def cargar(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    data = json.load(f)
                    print(f"DEBUG: Datos cargados de {self.archivo}: {data}") # DEBUG LINE
                    return data
            print(f"DEBUG: Archivo {self.archivo} no encontrado o vacío. Retornando {{}}.") # DEBUG LINE
        except json.JSONDecodeError as e:
            messagebox.showerror("Error de JSON", f"Error al decodificar {self.archivo}: {e}")
            print(f"ERROR: JSONDecodeError en {self.archivo}: {e}") # DEBUG LINE
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo {self.archivo}: {str(e)}")
            print(f"ERROR: Excepción al cargar {self.archivo}: {e}") # DEBUG LINE
        return {}

    def guardar(self, data):
        try:
            with open(self.archivo, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")

    def crear_usuario(self, email, password, rol="cliente"):
        usuarios = self.cargar()
        if email in usuarios:
            return False
        usuarios[email] = {"password": password, "rol": rol, "email": email} 
        self.guardar(usuarios)
        return True

    def validar_usuario(self, email, password):
        usuarios = self.cargar()
        print(f"DEBUG: Intentando validar usuario: '{email}', contraseña introducida: '{password}'") 

        if email not in usuarios:
            print(f"DEBUG: El email '{email}' NO existe como clave en el diccionario de usuarios.") # NUEVA LÍNEA DEBUG
            return None

        # Si el email existe, ahora verificamos la contraseña
        stored_password = usuarios[email]["password"]
        print(f"DEBUG: Contraseña almacenada para '{email}': '{stored_password}'") # NUEVA LÍNEA DEBUG

        if stored_password == password:
            print(f"DEBUG: Usuario '{email}' validado correctamente.")
            return usuarios[email]
        else:
            print(f"DEBUG: Las contraseñas NO coinciden para '{email}'.") # NUEVA LÍNEA DEBUG
            print(f"DEBUG: Tipo contraseña introducida: {type(password)}, Tipo contraseña almacenada: {type(stored_password)}") # NUEVA LÍNEA DEBUG
            return None

# Nueva ventana para el Recepcionista
class ventanaRecepcionista:
    def __init__(self, master=None):
        self.master = master
        self.ventana = tk.Toplevel(master) 
        self.ventana.title("Menú de Recepcionista")
        self.ventana.geometry("300x200")

        tk.Label(self.ventana, text="Bienvenido Recepcionista", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.ventana, text="Gestión de Reservas", command=self.abrir_gestion_reservas).pack(pady=10)
        tk.Button(self.ventana, text="Gestión de Servicios", command=self.abrir_gestion_servicios).pack(pady=10)

    def abrir_gestion_reservas(self):
        ventanaCRUDreservas() 

    def abrir_gestion_servicios(self):
        ventanaCRUDservicios() 


# Nueva ventana para la gestión de recepcionistas por el Admin
class ventanaCRUDrecepcionistas:
    def __init__(self, user_manager): 
        self.user_manager = user_manager
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Recepcionistas")
        self.ventana.geometry("400x300")

        tk.Label(self.ventana, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.ventana)
        self.email_entry.pack(pady=5)

        tk.Label(self.ventana, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self.ventana, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.ventana, text="Crear Recepcionista", command=self.crear_recepcionista).pack(pady=10)

        # Mostrar lista de recepcionistas existentes
        self.tree = ttk.Treeview(self.ventana, columns=("Email",), show="headings")
        self.tree.heading("Email", text="Email")
        self.tree.pack(pady=10, fill="both", expand=True)
        self.cargar_recepcionistas_en_tabla()


    def crear_recepcionista(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Formato de correo electrónico inválido.")
            return

        if not email or not password:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        
        if self.user_manager.crear_usuario(email, password, "recepcionista"):
            messagebox.showinfo("Éxito", "Recepcionista creado exitosamente.")
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.cargar_recepcionistas_en_tabla()
        else:
            messagebox.showerror("Error", "El email ya está registrado.")

    def cargar_recepcionistas_en_tabla(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        usuarios = self.user_manager.cargar()
        for email, data in usuarios.items():
            if data.get("rol") == "recepcionista":
                self.tree.insert("", "end", values=(email,))

class ventanaAcceso:
    def __init__(self, master):
        self.master = master
        self.user_manager = gestionUsuarios()
        #  NUEVA LÓGICA PARA ASEGURAR QUE EL ADMIN EXISTA 
        # Cargar usuarios para verificar si el admin ya existe
        usuarios_existentes = self.user_manager.cargar() # Esto intenta cargar el JSON
        if "admin@hotel.com" not in usuarios_existentes or \
           usuarios_existentes.get("admin@hotel.com", {}).get("rol") != "admin":
            # Si el admin no existe o su rol no es 'admin', lo creamos
            self.user_manager.crear_usuario("admin@hotel.com", "admin123", "admin")
            print("DEBUG: Admin user 'admin@hotel.com' created/ensured.")
        

        self.frame = tk.Frame(master, bg="lightgray", bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        

        self.frame = tk.Frame(master, bg="lightgray", bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame, text="Iniciar Sesión", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.frame, text="Correo Electrónico:").pack(pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack(pady=5)

        tk.Label(self.frame, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.frame, text="Iniciar Sesión", command=self.login).pack(pady=10)
        tk.Button(self.frame, text="Registrarse", command=self.register).pack(pady=5)

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Formato de correo electrónico inválido.")
            return

        if not email or not password:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if self.user_manager.crear_usuario(email, password, "cliente"):
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente como cliente.")
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El email ya está registrado.")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        try:
            logged_user = self.user_manager.validar_usuario(email, password)

            if logged_user:
                messagebox.showinfo("Éxito", f"Bienvenido, {logged_user.get('email', email)}")
                self.master.destroy()  # Cierra la ventana de login

                if logged_user["rol"] == "admin":
                    menu_admin = tk.Toplevel()
                    menu_admin.title("Menú de Administrador")
                    menu_admin.geometry("300x350")

                    tk.Button(menu_admin, text="Gestión de Recepcionistas",
                            command=lambda: ventanaCRUDrecepcionistas(self.user_manager)).pack(pady=10) 

                    tk.Button(menu_admin, text="Gestión de Clientes",
                            command=ventanaCRUDclientes).pack(pady=10)

                    tk.Button(menu_admin, text="Gestión de Roles",
                            command=ventanaCRUDroles).pack(pady=10)

                    tk.Button(menu_admin, text="Gestión de Reservas",
                            command=ventanaCRUDreservas).pack(pady=10)

                    tk.Button(menu_admin, text="Gestión de Habitaciones",
                            command=GestionHabitaciones).pack(pady=10)

                    tk.Button(menu_admin, text="Gestión de Servicios Adicionales",
                            command=ventanaCRUDservicios).pack(pady=10) 

                elif logged_user["rol"] == "recepcionista":
                    ventanaRecepcionista(None)
                else: 
                    ventanaCliente(logged_user)

            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al iniciar sesión: {str(e)}")