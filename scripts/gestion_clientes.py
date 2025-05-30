import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import re

ARCHIVO_CLIENTES = "clientes.json"
ARCHIVO_RESERVAS = "reservas.json"

class ventanaCliente:
    def __init__(self, datos_usuario):
        self.usuario = datos_usuario
        self.reservas = self.cargar_reservas()

        self.ventana = tk.Toplevel()
        self.ventana.title("Panel del Cliente")
        self.ventana.geometry("500x400")

        tk.Label(self.ventana, text=f"Bienvenido, {self.usuario['email']}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.ventana, text="Ver mis datos", command=self.ver_datos).pack(pady=10)
        tk.Button(self.ventana, text="Ver mis reservas", command=self.ver_reservas).pack(pady=10)

    def cargar_reservas(self):
        if os.path.exists("reservas.json"):
            with open("reservas.json", "r") as f:
                return json.load(f)
        return {}

    def ver_datos(self):
        info = f"Correo: {self.usuario['email']}\nContraseña: {self.usuario['password']}\nRol: {self.usuario['rol']}"
        messagebox.showinfo("Mis datos", info)
    
    def ver_reservas(self):
        lista = [r for r in self.reservas.values() if r["cliente_id"] == self.usuario["email"]]

        if not lista:
            messagebox.showinfo("Reservas", "No tienes reservas registradas.")
            return

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Mis Reservas")
        ventana.geometry("400x300")

        for reserva in lista:
            texto = f"Habitación: {reserva['habitacion']}\nEntrada: {reserva['entrada']}\nSalida: {reserva['salida']}"
            tk.Label(ventana, text=texto, relief="groove", padx=10, pady=5).pack(pady=5, fill="x")

def cargar_clientes():
    if os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "r") as f:
            return json.load(f)
    return {}

def guardar_clientes(data):
    with open(ARCHIVO_CLIENTES, "w") as f:
        json.dump(data, f, indent=4)

def cargar_reservas():
    if os.path.exists(ARCHIVO_RESERVAS):
        with open(ARCHIVO_RESERVAS, "r") as f:
            return json.load(f)
    return {}

def verificacion(correo):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(regex, correo)

def guardar_reservas(data):
    with open(ARCHIVO_RESERVAS, "w") as f:
        json.dump(data, f, indent=4)

class ventanaCRUDclientes:
    def __init__(self):
        self.clientes = cargar_clientes()
        self.reservas = cargar_reservas()

        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("900x500")

        self.tree = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Correo", "Teléfono"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.pack(pady=10, fill="both", expand=True)

        self.actualizar_tabla()

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_cliente).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Editar", command=self.editar_cliente).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_cliente).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Reservar", command=self.hacer_reserva).grid(row=0, column=3, padx=5)

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        for id_cliente, data in self.clientes.items():
            self.tree.insert("", "end", values=(id_cliente, data["nombre"], data["correo"], data["telefono"]))

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
            if id_cliente not in self.clientes:
                messagebox.showerror("Error", f"No se encontró al cliente con ID '{id_cliente}'")
                return
            if messagebox.askyesno("Confirmar", f"¿Eliminar al cliente {id_cliente}?"):
                self.clientes.pop(id_cliente)
                guardar_clientes(self.clientes)
                self.actualizar_tabla()

    def ventana_formulario(self, titulo, id_cliente=None):
        ventana = tk.Toplevel(self.ventana)
        ventana.title(titulo)

        cliente = self.clientes.get(id_cliente, {})

        tk.Label(ventana, text="ID:").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack()
        if id_cliente:
            id_entry.insert(0, id_cliente)
            id_entry.config(state="disabled")

        tk.Label(ventana, text="Nombre:").pack()
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack()
        nombre_entry.insert(0, cliente.get("nombre", ""))

        tk.Label(ventana, text="Correo:").pack()
        correo_entry = tk.Entry(ventana)
        correo_entry.pack()
        correo_entry.insert(0, cliente.get("correo", ""))

        tk.Label(ventana, text="Teléfono:").pack()
        tel_entry = tk.Entry(ventana)
        tel_entry.pack()
        tel_entry.insert(0, cliente.get("telefono", ""))

        def guardar():
            id_val = id_cliente if id_cliente else id_entry.get().strip()
            nuevo = {
                "nombre": nombre_entry.get().strip(),
                "correo": correo_entry.get().strip(),
                "telefono": tel_entry.get().strip()
            }

            if not verificacion(nuevo["correo"]):
                messagebox.showwarning("Error", "Correo inválido.")
                return
            
            if not id_val or not nuevo["nombre"]:
                messagebox.showwarning("Error", "ID y nombre son obligatorios.")
                return
            
            self.clientes[id_val] = nuevo
            guardar_clientes(self.clientes)
            self.actualizar_tabla()
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    def hacer_reserva(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona un cliente para reservar.")
            return

        id_cliente = self.tree.item(seleccion[0])["values"][0]

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Nueva Reserva")

        tk.Label(ventana, text="Habitación #:").pack()
        habitacion_entry = tk.Entry(ventana)
        habitacion_entry.pack()

        tk.Label(ventana, text="Fecha entrada (YYYY-MM-DD):").pack()
        entrada_entry = tk.Entry(ventana)
        entrada_entry.pack()

        tk.Label(ventana, text="Fecha salida (YYYY-MM-DD):").pack()
        salida_entry = tk.Entry(ventana)
        salida_entry.pack()

        def guardar_reserva():
            habitacion = habitacion_entry.get().strip()
            entrada = entrada_entry.get().strip()
            salida = salida_entry.get().strip()

            try:
                datetime.strptime(entrada, "%Y-%m-%d")
                datetime.strptime(salida, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Error", "Formato de fecha inválido.")
                return
            entrada_dt = datetime.strptime(entrada, "%Y-%m-%d")
            salida_dt = datetime.strptime(salida, "%Y-%m-%d")

            for r in self.reservas.values():
                if r["habitacion"] ==habitacion:
                    r_entrada=datetime.strftime(r["entrada"], "%Y-%m-%d")
                    r_salida=datetime.strftime(r["salida"], "%Y-%m-%d")
                    if not (salida_dt <= r_entrada or entrada_dt >= r_salida):
                        messagebox.showwarning("Conflicto", "Ya hay una reserva en esa habitación en esas fechas.")
                        return


            reserva = {
                "cliente_id": id_cliente,
                "habitacion": habitacion,
                "entrada": entrada,
                "salida": salida
            }

            clave = f"{id_cliente}_{entrada}_{salida}"
            self.reservas[clave] = reserva
            guardar_reservas(self.reservas)
            messagebox.showinfo("Éxito", "Reserva guardada.")
            ventana.destroy()

        tk.Button(ventana, text="Confirmar Reserva", command=guardar_reserva).pack(pady=10)