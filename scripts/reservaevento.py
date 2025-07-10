import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os
from datetime import datetime, timedelta

ARCHIVO_RESERVAS = "reservas_eventos.json"
ARCHIVO_ESPACIOS = "espacios_evento.json"

def cargar_datos(archivo):
    if not os.path.exists(archivo):
        with open(archivo, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_reservas(reservas):
    with open(ARCHIVO_RESERVAS, "w") as f:
        json.dump(reservas, f, indent=4)

class ReservaEvento(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Reserva de Espacios para Eventos")
        menu_width = 950
        menu_height = 700
        self.geometry(f"{menu_width}x{menu_height}")
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (menu_width // 2)
        y = (screen_height // 2) - (menu_height // 2)
        self.geometry(f"{menu_width}x{menu_height}+{x}+{y}")
        self.configure(bg="#add8e6")

        estilo = ttk.Style(self)
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

        self.espacios = cargar_datos(ARCHIVO_ESPACIOS)
        self.reservas = cargar_datos(ARCHIVO_RESERVAS)
        self.crear_widgets()
        self.actualizar_combos()
        self.mostrar_reservas()

    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, style="Azul.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Lista de reservas
        columnas = ("id_espacio", "nombre_evento", "fecha", "personas", "contacto")
        self.tree = ttk.Treeview(main_frame, columns=columnas, show="headings", height=15)
        
        for col in columnas:
            self.tree.heading(col, text=col.capitalize().replace("_", " "))
            self.tree.column(col, width=120, anchor="center")
        
        self.tree.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        
        # Frame de formulario
        form_frame = ttk.LabelFrame(main_frame, text="Nueva Reserva", style="Azul.TLabelframe")
        form_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        # Campos del formulario
        campos = [
            ("Espacio:", "combo_espacio"),
            ("Nombre Evento:", "entry_nombre"),
            ("Fecha:", "cal_fecha"),
            ("N° Personas:", "entry_personas"),
            ("Contacto:", "entry_contacto")
        ]
        
        self.widgets = {}
        for i, (label, name) in enumerate(campos):
            tk.Label(form_frame, text=label, font=("Arial", 12), fg="#0d47a1", bg="#add8e6").grid(row=i, column=0, padx=5, pady=5, sticky="e")
            
            if name == "combo_espacio":
                combo = ttk.Combobox(form_frame, state="readonly")
                combo.grid(row=i, column=1, padx=5, pady=5, sticky="we")
                self.widgets[name] = combo
            elif name == "cal_fecha":
                cal = DateEntry(form_frame, date_pattern="yyyy-mm-dd", mindate=datetime.now() + timedelta(days=14))
                cal.grid(row=i, column=1, padx=5, pady=5, sticky="we")
                self.widgets[name] = cal
            else:
                entry = tk.Entry(form_frame)
                entry.grid(row=i, column=1, padx=5, pady=5, sticky="we")
                self.widgets[name] = entry
        
        ttk.Button(form_frame, text="Crear Reserva", style="Azul.TButton", command=self.crear_reserva).grid(
            row=len(campos), column=0, columnspan=2, pady=10)
        
        # Botones de acciones
        btn_frame = ttk.Frame(main_frame, style="Azul.TFrame")
        btn_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Cancelar Reserva", style="Azul.TButton", command=self.cancelar_reserva).pack(side=tk.LEFT, padx=5)

    def actualizar_combos(self):
        espacios_ids = [e["id"] for e in self.espacios]
        self.widgets["combo_espacio"]["values"] = espacios_ids
        if espacios_ids:
            self.widgets["combo_espacio"].current(0)

    def mostrar_reservas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for reserva in self.reservas:
            self.tree.insert("", "end", values=(
                reserva["id_espacio"],
                reserva["nombre_evento"],
                reserva["fecha"],
                reserva["personas"],
                reserva["contacto"]
            ))

    def crear_reserva(self):
        datos = {
            "id_espacio": self.widgets["combo_espacio"].get(),
            "nombre_evento": self.widgets["entry_nombre"].get().strip(),
            "fecha": self.widgets["cal_fecha"].get_date(),
            "personas": self.widgets["entry_personas"].get().strip(),
            "contacto": self.widgets["entry_contacto"].get().strip()
        }
        
        # Validaciones
        if not all(datos.values()):
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return
        
        if not datos["personas"].isdigit() or int(datos["personas"]) <= 0:
            messagebox.showwarning("Error", "Número de personas inválido")
            return
        
        # Validar fecha (mínimo 2 semanas)
        fecha_reserva = datetime.strptime(datos["fecha"], "%Y-%m-%d")
        if fecha_reserva < datetime.now() + timedelta(days=14):
            messagebox.showwarning("Error", "Reserva debe tener al menos 2 semanas de anticipación")
            return
        
        # Validar capacidad
        espacio = next((e for e in self.espacios if e["id"] == datos["id_espacio"]), None)
        if not espacio:
            messagebox.showwarning("Error", "Espacio no encontrado")
            return
        
        if int(datos["personas"]) > espacio["capacidad"]:
            messagebox.showwarning("Error", f"Capacidad excedida (Máx: {espacio['capacidad']})")
            return
        
        # Validar disponibilidad de fecha
        if any(r for r in self.reservas if r["id_espacio"] == datos["id_espacio"] and r["fecha"] == datos["fecha"]):
            messagebox.showwarning("Error", "Espacio ya reservado para esa fecha")
            return
        
        # Crear reserva
        datos["personas"] = int(datos["personas"])
        self.reservas.append(datos)
        guardar_reservas(self.reservas)
        self.mostrar_reservas()
        
        # Limpiar campos
        self.widgets["entry_nombre"].delete(0, tk.END)
        self.widgets["entry_personas"].delete(0, tk.END)
        self.widgets["entry_contacto"].delete(0, tk.END)
        
        messagebox.showinfo("Éxito", "Reserva creada correctamente")

    def cancelar_reserva(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione una reserva")
            return
        
        item = seleccionado[0]
        valores = self.tree.item(item, "values")
        
        if messagebox.askyesno("Confirmar", "¿Cancelar esta reserva?"):
            self.reservas = [r for r in self.reservas if not (
                r["id_espacio"] == valores[0] and
                r["fecha"] == valores[2]
            )]
            
            guardar_reservas(self.reservas)
            self.mostrar_reservas()
            messagebox.showinfo("Éxito", "Reserva cancelada")
