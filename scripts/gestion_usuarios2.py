from .users import User
from .gestion_clientes import ventanaCRUDclientes, ventanaCliente
from .gestion_rol import ventanaCRUDroles, cargarRoles
from .gestion_reservas import ventanaCRUDreservas
from .gestion_habitaciones import GestionHabitaciones
from .gestion_servicios import ventanaCRUDservicios 
from .crearespacioevento import GestionEspaciosEvento
from .reservaevento import ReservaEvento


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
        self.archivo = "usuarios.json" # Archivo para guardar usuarios

    def cargar(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    datos = json.load(f)
                    print(f"DEBUG: Datos cargados de {self.archivo}: {datos}") # Línea de depuración
                    return datos
            print(f"DEBUG: Archivo {self.archivo} no encontrado o vacío. Retornando {{}}.") # Línea de depuración
        except json.JSONDecodeError as e:
            messagebox.showerror("Error de JSON", f"Error al decodificar {self.archivo}: {e}")
            print(f"ERROR: JSONDecodeError en {self.archivo}: {e}") # Línea de depuración
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo {self.archivo}: {str(e)}")
            print(f"ERROR: Excepción al cargar {self.archivo}: {e}") # Línea de depuración
        return {}

    def guardar(self, datos):
        try:
            with open(self.archivo, 'w') as f:
                json.dump(datos, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")

    def crear_usuario(self, correo, contrasena, rol="cliente"):
        usuarios = self.cargar()
        if correo in usuarios:
            return False # El correo ya está registrado
        usuarios[correo] = {"password": contrasena, "rol": rol, "email": correo}
        self.guardar(usuarios)
        return True

    # Función para actualizar un usuario existente
    def actualizar_usuario(self, correo_original, nuevo_correo, nueva_contrasena, nuevo_rol):
        usuarios = self.cargar()
        if correo_original not in usuarios:
            return False # El usuario no existe

        # Si el correo cambia, verificar que el nuevo correo no esté ya en uso por otro usuario
        if correo_original != nuevo_correo and nuevo_correo in usuarios:
            return False # El nuevo correo ya está en uso

        # Actualizar los datos del usuario
        usuario_actualizado = {
            "password": nueva_contrasena,
            "rol": nuevo_rol,
            "email": nuevo_correo
        }

        if correo_original != nuevo_correo:
            # Si el correo cambió, eliminamos la entrada antigua y agregamos la nueva
            del usuarios[correo_original]
            usuarios[nuevo_correo] = usuario_actualizado
        else:
            # Si el correo no cambió, simplemente actualizamos la entrada existente
            usuarios[correo_original] = usuario_actualizado

        self.guardar(usuarios)
        return True

    # Función para eliminar un usuario
    def eliminar_usuario(self, correo):
        usuarios = self.cargar()
        if correo in usuarios:
            del usuarios[correo]
            self.guardar(usuarios)
            return True
        return False


    def validar_usuario(self, correo, contrasena):
        usuarios = self.cargar()
        print(f"DEBUG: Intentando validar usuario: '{correo}', contraseña introducida: '{contrasena}'") # Línea de depuración

        if correo not in usuarios:
            print(f"DEBUG: El email '{correo}' NO existe como clave en el diccionario de usuarios.") # Línea de depuración
            return None

        # Si el correo existe, ahora verificamos la contraseña
        contrasena_guardada = usuarios[correo]["password"]
        print(f"DEBUG: Contraseña almacenada para '{correo}': '{contrasena_guardada}'") # Línea de depuración

        if contrasena_guardada == contrasena:
            print(f"DEBUG: Usuario '{correo}' validado correctamente.")
            return usuarios[correo]
        else:
            print(f"DEBUG: Las contraseñas NO coinciden para '{correo}'.") # Línea de depuración
            print(f"DEBUG: Tipo contraseña introducida: {type(contrasena)}, Tipo contraseña almacenada: {type(contrasena_guardada)}") 
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



class ventanaCRUDrecepcionistas:
    def __init__(self, gestor_usuarios): 
        self.gestor_usuarios = gestor_usuarios
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Recepcionistas")
        self.ventana.geometry("600x450") 

        # Marco para los campos de entrada
        marco_entradas = tk.Frame(self.ventana)
        marco_entradas.pack(pady=10)

        tk.Label(marco_entradas, text="Correo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entrada_correo = tk.Entry(marco_entradas)
        self.entrada_correo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(marco_entradas, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entrada_contrasena = tk.Entry(marco_entradas, show="*")
        self.entrada_contrasena.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Guardar la referencia al correo original cuando se edita
        self.correo_original_seleccionado = None

        
        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=10)

        tk.Button(marco_botones, text="Crear Recepcionista", command=self.crear_recepcionista).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="Editar Recepcionista", command=self.editar_recepcionista).grid(row=0, column=1, padx=5)
        tk.Button(marco_botones, text="Eliminar Recepcionista", command=self.eliminar_recepcionista).grid(row=0, column=2, padx=5)
        tk.Button(marco_botones, text="Limpiar Campos", command=self.limpiar_campos).grid(row=0, column=3, padx=5)


        # Mostrar lista de recepcionistas existentes
        columnas = ("Correo",)
        self.arbol = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        self.arbol.heading("Correo", text="Correo")
        self.arbol.pack(pady=10, fill="both", expand=True)

        # Vincular la selección del Treeview a una función para cargar datos
        self.arbol.bind("<<TreeviewSelect>>", self.cargar_datos_seleccionados)

        self.cargar_recepcionistas_en_tabla()

    def limpiar_campos(self):
        self.entrada_correo.delete(0, tk.END)
        self.entrada_contrasena.delete(0, tk.END)
        self.correo_original_seleccionado = None # Restablecer la referencia al original


    def crear_recepcionista(self):
        correo = self.entrada_correo.get().strip()
        contrasena = self.entrada_contrasena.get().strip()

        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "Formato de correo electrónico inválido.")
            return

        if not correo or not contrasena:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Si hay un recepcionista seleccionado, se asume que se quiere actualizar, no crear
        # Esto previene la creación accidental si se olvidó limpiar los campos
        if self.correo_original_seleccionado:
            messagebox.showwarning("Advertencia", "Un recepcionista ya está seleccionado para edición. Limpie los campos si desea crear uno nuevo.")
            return

        if self.gestor_usuarios.crear_usuario(correo, contrasena, "recepcionista"):
            messagebox.showinfo("Éxito", "Recepcionista creado exitosamente.")
            self.limpiar_campos()
            self.cargar_recepcionistas_en_tabla()
        else:
            messagebox.showerror("Error", "El correo ya está registrado.")

    def editar_recepcionista(self):
        # Obtener el recepcionista seleccionado
        seleccion = self.arbol.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione un recepcionista para editar.")
            return

        # Obtener los datos actuales de los campos de entrada
        nuevo_correo = self.entrada_correo.get().strip()
        nueva_contrasena = self.entrada_contrasena.get().strip()

        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", nuevo_correo):
            messagebox.showerror("Error", "Formato de correo electrónico inválido para la edición.")
            return

        if not nuevo_correo or not nueva_contrasena:
            messagebox.showerror("Error", "Los campos de correo y contraseña son obligatorios para la edición.")
            return

        # Usar la referencia al correo original que se guardó al seleccionar
        correo_a_editar = self.correo_original_seleccionado

        if not correo_a_editar: # Debería estar establecido por cargar_datos_seleccionados
             messagebox.showerror("Error interno", "No se pudo determinar el recepcionista original a editar.")
             return

        # Intentar actualizar el usuario
        # Asegurarse de que el rol se mantenga como "recepcionista"
        if self.gestor_usuarios.actualizar_usuario(correo_a_editar, nuevo_correo, nueva_contrasena, "recepcionista"):
            messagebox.showinfo("Éxito", f"Recepcionista '{correo_a_editar}' editado exitosamente a '{nuevo_correo}'.")
            self.limpiar_campos()
            self.cargar_recepcionistas_en_tabla()
        else:
            # Aquí, la falla podría ser porque el nuevo correo ya existe (si se cambió)
            messagebox.showerror("Error de edición", "No se pudo editar el recepcionista. El nuevo correo ya podría estar en uso.")


    def eliminar_recepcionista(self):
        seleccion = self.arbol.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione un recepcionista para eliminar.")
            return

        # Obtener el correo del recepcionista seleccionado
        correo_a_eliminar = self.arbol.item(seleccion[0], "values")[0]

        if messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar al recepcionista '{correo_a_eliminar}'?"):
            if self.gestor_usuarios.eliminar_usuario(correo_a_eliminar):
                messagebox.showinfo("Éxito", "Recepcionista eliminado exitosamente.")
                self.limpiar_campos()
                self.cargar_recepcionistas_en_tabla()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el recepcionista.")

    def cargar_datos_seleccionados(self, event):
        """
        Carga los datos del recepcionista seleccionado en los campos de entrada.
        """
        seleccion = self.arbol.selection()
        if seleccion:
            item = seleccion[0]
            correo_seleccionado = self.arbol.item(item, "values")[0]

            usuarios = self.gestor_usuarios.cargar()
            recepcionista_data = usuarios.get(correo_seleccionado)

            if recepcionista_data:
                self.entrada_correo.delete(0, tk.END)
                self.entrada_correo.insert(0, recepcionista_data.get("email", ""))
                self.entrada_contrasena.delete(0, tk.END)
                self.entrada_contrasena.insert(0, recepcionista_data.get("password", ""))
                self.correo_original_seleccionado = correo_seleccionado # Guardar la referencia al correo original


    def cargar_recepcionistas_en_tabla(self):
        for i in self.arbol.get_children():
            self.arbol.delete(i)

        usuarios = self.gestor_usuarios.cargar()
        for correo, datos in usuarios.items():
            if datos.get("rol") == "recepcionista":
                self.arbol.insert("", "end", values=(correo,))

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
                    
                    tk.Button(menu_admin, text="Gestión Espacios de Eventos",
                            command= GestionEspaciosEvento).pack(pady=10)
                    
                    tk.Button(menu_admin, text="Reservas de Eventos",
                            command= ReservaEvento).pack(pady=10)
                    

                elif logged_user["rol"] == "recepcionista":
                    ventanaRecepcionista(None)
                else: 
                    ventanaCliente(logged_user)

            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al iniciar sesión: {str(e)}")