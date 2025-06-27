import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

ARCHIVO_ESPACIOS = "espacios_evento.json"

def cargar_espacios():
    if not os.path.exists(ARCHIVO_ESPACIOS):
        with open(ARCHIVO_ESPACIOS, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(ARCHIVO_ESPACIOS, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_espacios(espacios):
    with open(ARCHIVO_ESPACIOS, "w") as f:
        json.dump(espacios, f, indent=4)

class GestionEspaciosEvento(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gestión de Espacios para Eventos")
        self.geometry("800x600")
        self.resizable(False, False)
        
        self.espacios = cargar_espacios()
        self.crear_widgets()
        self.mostrar_espacios()

    def crear_widgets(self):
        # Treeview para mostrar espacios
        columnas = ("id", "nombre", "tipo", "capacidad", "ubicacion")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings", height=10)
        
        for col in columnas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=150, anchor="center")
        
        self.tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Frame de botones
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Editar", command=self.editar_espacio).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_espacio).pack(side=tk.LEFT, padx=5)
        
        # Formulario
        form_frame = tk.LabelFrame(self, text="Nuevo Espacio")
        form_frame.pack(pady=10, padx=10, fill=tk.X)
        
        campos = [
            ("ID Espacio:", "entry_id"),
            ("Nombre:", "entry_nombre"),
            ("Tipo (Abierto/Cerrado):", "entry_tipo"),
            ("Capacidad:", "entry_capacidad"),
            ("Ubicación:", "entry_ubicacion")
        ]
        
        self.entries = {}
        for i, (label, var_name) in enumerate(campos):
            tk.Label(form_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(form_frame)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="we")
            self.entries[var_name] = entry
        
        btn_agregar = tk.Button(form_frame, text="Agregar Espacio", command=self.agregar_espacio)
        btn_agregar.grid(row=len(campos), column=0, columnspan=2, pady=10)

    def mostrar_espacios(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for espacio in self.espacios:
            self.tree.insert("", "end", values=(
                espacio["id"],
                espacio["nombre"],
                espacio["tipo"],
                espacio["capacidad"],
                espacio["ubicacion"]
            ))

    def agregar_espacio(self):
        datos = {
            "id": self.entries["entry_id"].get().strip(),
            "nombre": self.entries["entry_nombre"].get().strip(),
            "tipo": self.entries["entry_tipo"].get().strip(),
            "capacidad": self.entries["entry_capacidad"].get().strip(),
            "ubicacion": self.entries["entry_ubicacion"].get().strip()
        }
        
        # Validaciones
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
        self.mostrar_espacios()
        
        # Limpiar campos
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        
        messagebox.showinfo("Éxito", "Espacio agregado correctamente")

    def editar_espacio(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un espacio")
            return
        
        item = seleccionado[0]
        valores = self.tree.item(item, "values")
        espacio_id = valores[0]
        
        # Buscar espacio
        espacio = next((e for e in self.espacios if e["id"] == espacio_id), None)
        if not espacio:
            return
        
        # Ventana de edición
        ventana_editar = tk.Toplevel(self)
        ventana_editar.title("Editar Espacio")
        ventana_editar.resizable(False, False)
        
        campos = [
            ("Nombre:", espacio["nombre"]),
            ("Tipo:", espacio["tipo"]),
            ("Capacidad:", espacio["capacidad"]),
            ("Ubicación:", espacio["ubicacion"])
        ]
        
        entries_editar = {}
        for i, (label, valor) in enumerate(campos):
            tk.Label(ventana_editar, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(ventana_editar)
            entry.insert(0, str(valor))
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries_editar[label] = entry
        
        def guardar_cambios():
            nuevos_datos = {
                "nombre": entries_editar["Nombre:"].get().strip(),
                "tipo": entries_editar["Tipo:"].get().strip(),
                "capacidad": entries_editar["Capacidad:"].get().strip(),
                "ubicacion": entries_editar["Ubicación:"].get().strip()
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
            self.mostrar_espacios()
            ventana_editar.destroy()
            messagebox.showinfo("Éxito", "Espacio actualizado")
        
        tk.Button(ventana_editar, text="Guardar", command=guardar_cambios).grid(row=len(campos), column=0, columnspan=2, pady=10)

    def eliminar_espacio(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un espacio")
            return
        
        item = seleccionado[0]
        valores = self.tree.item(item, "values")
        espacio_id = valores[0]
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar espacio {espacio_id}?"):
            self.espacios = [e for e in self.espacios if e["id"] != espacio_id]
            guardar_espacios(self.espacios)
            self.mostrar_espacios()
            messagebox.showinfo("Éxito", "Espacio eliminado")
