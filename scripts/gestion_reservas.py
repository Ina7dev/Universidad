import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime, timedelta

ARCHIVO_RESERVAS = "reservas.json"
ARCHIVO_CLIENTES = "clientes.json"

def cargar_reservas():
    if os.path.exists(ARCHIVO_RESERVAS):
        with open(ARCHIVO_RESERVAS, "r") as f:
            return json.load(f)
    return {}

def guardar_reservas(data):
    with open(ARCHIVO_RESERVAS, "w") as f:
        json.dump(data, f, indent=4)

def cargar_clientes():
    if os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "r") as f:
            return json.load(f)
    return {}

class ventanaCRUDreservas:
    def __init__(self):
        self.reservas = cargar_reservas()
        self.clientes = cargar_clientes()

        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Reservas")
        self.ventana.geometry("900x600")

        # Treeview para mostrar reservas
        columns = ("ID", "Cliente", "Piso", "Tipo", "Personas", "Hab.", "Entrada", "Salida", "Noches")
        self.tree = ttk.Treeview(self.ventana, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="both", expand=True)

        # Formulario para CRUD
        form_frame = tk.Frame(self.ventana)
        form_frame.pack(pady=10)

        # Cliente
        tk.Label(form_frame, text="Cliente:").grid(row=0, column=0, sticky="e")
        self.cliente_var = tk.StringVar()
        clientes_ids = list(self.clientes.keys())
        self.cliente_combo = ttk.Combobox(form_frame, values=clientes_ids, textvariable=self.cliente_var, state="readonly")
        self.cliente_combo.grid(row=0, column=1)

        # Piso
        tk.Label(form_frame, text="Piso:").grid(row=1, column=0, sticky="e")
        self.piso_var = tk.StringVar()
        self.piso_combo = ttk.Combobox(form_frame, values=["1", "2", "3"], textvariable=self.piso_var, state="readonly")
        self.piso_combo.grid(row=1, column=1)
        self.piso_combo.bind("<<ComboboxSelected>>", self.actualizar_tipo_habitacion)

        # Tipo habitación
        tk.Label(form_frame, text="Tipo habitación:").grid(row=2, column=0, sticky="e")
        self.tipo_var = tk.StringVar()
        self.tipo_combo = ttk.Combobox(form_frame, values=[], textvariable=self.tipo_var, state="readonly")
        self.tipo_combo.grid(row=2, column=1)
        self.tipo_combo.bind("<<ComboboxSelected>>", self.actualizar_max_personas)

        # Cantidad personas
        tk.Label(form_frame, text="Personas:").grid(row=3, column=0, sticky="e")
        self.personas_var = tk.IntVar(value=1)
        self.personas_spin = tk.Spinbox(form_frame, from_=1, to=4, textvariable=self.personas_var, width=5)
        self.personas_spin.grid(row=3, column=1)

        # Fecha entrada
        tk.Label(form_frame, text="Fecha entrada (DD-MM-YYYY):").grid(row=4, column=0, sticky="e")
        self.entrada_entry = tk.Entry(form_frame)
        self.entrada_entry.grid(row=4, column=1)

        # Cantidad noches
        tk.Label(form_frame, text="Cantidad noches:").grid(row=5, column=0, sticky="e")
        self.noches_var = tk.IntVar(value=1)
        self.noches_spin = tk.Spinbox(form_frame, from_=1, to=30, textvariable=self.noches_var, width=5)
        self.noches_spin.grid(row=5, column=1)

        # Botones
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Agregar", command=self.agregar_reserva).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Editar", command=self.editar_reserva).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_reserva).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Limpiar", command=self.limpiar_form).grid(row=0, column=3, padx=5)

        self.actualizar_tabla()

    def actualizar_tipo_habitacion(self, event=None):
        piso = self.piso_var.get()
        if piso in ["1", "2"]:
            # Pisos 1 y 2 solo estándar
            self.tipo_combo.config(values=["Estándar"])
            self.tipo_var.set("Estándar")
            self.personas_spin.config(from_=1, to=2)
            if self.personas_var.get() > 2:
                self.personas_var.set(2)
        elif piso == "3":
            # Piso 3 solo suites
            self.tipo_combo.config(values=["Suite"])
            self.tipo_var.set("Suite")
            self.personas_spin.config(from_=1, to=4)
        else:
            self.tipo_combo.config(values=[])
            self.tipo_var.set("")
            self.personas_spin.config(from_=1, to=4)

    def actualizar_max_personas(self, event=None):
        tipo = self.tipo_var.get()
        if tipo == "Estándar":
            self.personas_spin.config(from_=1, to=2)
            if self.personas_var.get() > 2:
                self.personas_var.set(2)
        elif tipo == "Suite":
            self.personas_spin.config(from_=1, to=4)
        else:
            self.personas_spin.config(from_=1, to=4)

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        for clave, res in self.reservas.items():
            entrada_fmt = datetime.strptime(res["entrada"], "%d-%m-%Y").strftime("%d-%m-%Y")
            salida_fmt = datetime.strptime(res["salida"], "%d-%m-%Y").strftime("%d-%m-%Y")
            self.tree.insert("", "end", iid=clave, values=(
                    clave,
                res["cliente_id"],
                res["piso"],
                res["tipo_habitacion"],
                res["personas"],
                res["habitacion"],
                entrada_fmt,
                salida_fmt,
                res["noches"],
        ))


    def validar_formulario(self):
        # Validar cliente seleccionado
        if not self.cliente_var.get():
            messagebox.showwarning("Error", "Selecciona un cliente")
            return False

        # Validar piso
        if self.piso_var.get() not in ["1", "2", "3"]:
            messagebox.showwarning("Error", "Selecciona un piso válido")
            return False

        # Validar tipo habitación
        if self.tipo_var.get() not in ["Estándar", "Suite"]:
            messagebox.showwarning("Error", "Selecciona un tipo de habitación válido")
            return False

        # Validar personas
        personas = self.personas_var.get()
        if self.tipo_var.get() == "Estándar" and (personas < 1 or personas > 2):
            messagebox.showwarning("Error", "Estándar admite máximo 2 personas")
            return False
        if self.tipo_var.get() == "Suite" and (personas < 1 or personas > 4):
            messagebox.showwarning("Error", "Suite admite máximo 4 personas")
            return False

        # Validar fecha entrada
        try:
            fecha_entrada = datetime.strptime(self.entrada_entry.get(), "%d-%m-%Y")
        except ValueError:
            messagebox.showwarning("Error", "Formato de fecha inválido (DD-MM-YYY)")
            return False

        # Validar noches
        noches = self.noches_var.get()
        if noches < 1:
            messagebox.showwarning("Error", "La cantidad de noches debe ser al menos 1")
            return False

        return True

    def generar_habitacion(self, piso, tipo):
        # Por simplicidad, numeramos habitaciones como piso + tipo + número correlativo.
        # Ejemplo: Piso 1 estándar: 101, 102, 103...
        # Piso 3 suite: 301, 302...
        # Buscamos la primer habitación libre para ese piso y tipo

        habitaciones_existentes = [
            r["habitacion"] for r in self.reservas.values()
            if r["piso"] == piso and r["tipo_habitacion"] == tipo
        ]

        # Definir máximo habitaciones por piso y tipo (ejemplo 10 por tipo)
        max_habs = 10

        for i in range(1, max_habs + 1):
            hab_num = f"{piso}0{i}"
            if hab_num not in habitaciones_existentes:
                return hab_num

        # Si no hay habitación libre
        return None

    def validar_conflicto_reserva(self, hab, entrada, salida, clave_actual=None):
        entrada_dt = datetime.strptime(entrada, "%d-%m-%Y")
        salida_dt = datetime.strptime(salida, "%d-%m-%Y")
        for clave, res in self.reservas.items():
            if clave == clave_actual:
                continue  # ignorar la reserva que estamos editando
            if res["habitacion"] == hab:
                res_entrada = datetime.strptime(res["entrada"], "%d-%m-%Y")
                res_salida = datetime.strptime(res["salida"], "%d-%m-%Y")
                # Si fechas se solapan
                if not (salida_dt <= res_entrada or entrada_dt >= res_salida):
                    return True
        return False

    def agregar_reserva(self):
        if not self.validar_formulario():
            return

        cliente = self.cliente_var.get()
        piso = self.piso_var.get()
        tipo = self.tipo_var.get()
        personas = self.personas_var.get()
        entrada = self.entrada_entry.get()
        noches = self.noches_var.get()

        # Calcular fecha salida
        entrada_dt = datetime.strptime(entrada, "%d-%m-%Y")
        salida_dt = entrada_dt + timedelta(days=noches)
        salida = salida_dt.strftime("%d-%m-%Y")

        habitacion = self.generar_habitacion(piso, tipo)
        if habitacion is None:
            messagebox.showerror("Error", "No hay habitaciones libres para ese piso y tipo")
            return

        # Validar que no haya conflicto
        if self.validar_conflicto_reserva(habitacion, entrada, salida):
            messagebox.showwarning("Conflicto", "Ya hay una reserva en esa habitación en esas fechas")
            return

        clave = f"{cliente}_{entrada}_{habitacion}"
        reserva = {
            "cliente_id": cliente,
            "piso": piso,
            "tipo_habitacion": tipo,
            "personas": personas,
            "habitacion": habitacion,
            "entrada": entrada,
            "salida": salida,
            "noches": noches
        }

        self.reservas[clave] = reserva
        guardar_reservas(self.reservas)
        messagebox.showinfo("Éxito", "Reserva agregada")
        self.actualizar_tabla()
        self.limpiar_form()

    def editar_reserva(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona una reserva para editar")
            return

        clave = seleccion[0]

        if not self.validar_formulario():
            return

        cliente = self.cliente_var.get()
        piso = self.piso_var.get()
        tipo = self.tipo_var.get()
        personas = self.personas_var.get()
        entrada = self.entrada_entry.get()
        noches = self.noches_var.get()

        entrada_dt = datetime.strptime(entrada, "%Y-%m-%d")
        salida_dt = entrada_dt + timedelta(days=noches)
        salida = salida_dt.strftime("%Y-%m-%d")

        habitacion = self.reservas[clave]["habitacion"]  # mantengo habitación asignada

        # Validar conflicto (ignorando esta reserva)
        if self.validar_conflicto_reserva(habitacion, entrada, salida, clave_actual=clave):
            messagebox.showwarning("Conflicto", "Ya hay una reserva en esa habitación en esas fechas")
            return

        reserva = {
            "cliente_id": cliente,
            "piso": piso,
            "tipo_habitacion": tipo,
            "personas": personas,
            "habitacion": habitacion,
            "entrada": entrada,
            "salida": salida,
            "noches": noches
        }

        self.reservas[clave] = reserva
        guardar_reservas(self.reservas)
        messagebox.showinfo("Éxito", "Reserva editada")
        self.actualizar_tabla()
        self.limpiar_form()

    def eliminar_reserva(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona una reserva para eliminar")
            return

        clave = seleccion[0]
        if messagebox.askyesno("Confirmar", "¿Eliminar la reserva seleccionada?"):
            self.reservas.pop(clave, None)
            guardar_reservas(self.reservas)
            self.actualizar_tabla()
            self.limpiar_form()

    def limpiar_form(self):
        self.cliente_var.set("")
        self.piso_var.set("")
        self.tipo_var.set("")
        self.personas_var.set(1)
        self.entrada_entry.delete(0, tk.END)
        self.noches_var.set(1)

    def cargar_datos_form(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return

        clave = seleccion[0]
        res = self.reservas.get(clave)
        if not res:
            return

        self.cliente_var.set(res["cliente_id"])
        self.piso_var.set(res["piso"])
        self.actualizar_tipo_habitacion()
        self.tipo_var.set(res["tipo_habitacion"])
        self.actualizar_max_personas()
        self.personas_var.set(res["personas"])
        self.entrada_entry.delete(0, tk.END)
        self.entrada_entry.insert(0, res["entrada"])
        self.noches_var.set(res["noches"])

# Para que al seleccionar en el treeview se cargue en el formulario
        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_form)
