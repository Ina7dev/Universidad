import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime, timedelta

ARCHIVO_RESERVAS = "reservas.json"
ARCHIVO_CLIENTES = "clientes.json"

def error_response(msg):
    messagebox.showwarning("Error", msg)

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
    return []

def cargar_habitaciones():
    if os.path.exists("habitaciones.json"):
        with open("habitaciones.json", "r") as f:
            return json.load(f)
    return []

def guardar_habitaciones(data):
    with open("habitaciones.json", "w") as f:
        json.dump(data, f, indent=4)

def set_estado_habitacion(id_hab, estado):
    habitaciones = cargar_habitaciones()
    for hab in habitaciones:
        if hab.get("id") == id_hab:
            hab["estado"] = estado
    guardar_habitaciones(habitaciones)

def habitacion_existe(id_hab):
    habitaciones = cargar_habitaciones()
    return any(h.get("id") == id_hab for h in habitaciones)

def habitacion_esta_ocupada(id_hab, entrada, salida, reservas, clave_actual=None):
    entrada_dt = datetime.strptime(entrada, "%d-%m-%Y")
    salida_dt = datetime.strptime(salida, "%d-%m-%Y")
    for clave, res in reservas.items():
        if clave == clave_actual:
            continue
        if res.get("habitacion") == id_hab:
            res_entrada = datetime.strptime(res["entrada"], "%d-%m-%Y")
            res_salida = datetime.strptime(res["salida"], "%d-%m-%Y")
            if not (salida_dt <= res_entrada or entrada_dt >= res_salida):
                return True
    return False

class ventanaCRUDreservas:
    def __init__(self, on_close=None):
        self.reservas = cargar_reservas()
        self.clientes = cargar_clientes()
        self.on_close = on_close

        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Reservas")
        self.ventana.geometry("1200x600")
        self.ventana.state('zoomed')
        self.ventana.protocol("WM_DELETE_WINDOW", self._on_close)
        self.ventana.bind("<Escape>", lambda e: self.ventana.destroy())  # Esc para cerrar

        #Live search
        search_frame = tk.Frame(self.ventana)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Buscar:").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._filtrar_reservas)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left")

        #mostrar reservas
        columns = ("ID", "Cliente", "Piso", "Tipo", "Personas", "Hab.", "Entrada", "Salida", "Noches")
        self.tree = ttk.Treeview(self.ventana, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="both", expand=True)

        #Formulario para el CRUD
        form_frame = tk.Frame(self.ventana)
        form_frame.pack(pady=10)

        #Cliente
        tk.Label(form_frame, text="Cliente:").grid(row=0, column=0, sticky="e")
        self.cliente_var = tk.StringVar()
        clientes_ids = [c.get("Correo", c.get("correo", "")) for c in self.clientes]
        self.cliente_combo = ttk.Combobox(form_frame, values=clientes_ids, textvariable=self.cliente_var, state="readonly")
        self.cliente_combo.grid(row=0, column=1)

        #piso
        tk.Label(form_frame, text="Piso:").grid(row=1, column=0, sticky="e")
        self.piso_var = tk.StringVar()
        self.piso_combo = ttk.Combobox(form_frame, values=["1", "2", "3"], textvariable=self.piso_var, state="readonly")
        self.piso_combo.grid(row=1, column=1)
        self.piso_combo.bind("<<ComboboxSelected>>", self.actualizar_tipo_habitacion)

        #tipo habitacion
        tk.Label(form_frame, text="Tipo habitación:").grid(row=2, column=0, sticky="e")
        self.tipo_var = tk.StringVar()
        self.tipo_combo = ttk.Combobox(form_frame, values=[], textvariable=self.tipo_var, state="readonly")
        self.tipo_combo.grid(row=2, column=1)
        self.tipo_combo.bind("<<ComboboxSelected>>", self.actualizar_max_personas)

        #cantidad de personas
        tk.Label(form_frame, text="Personas:").grid(row=3, column=0, sticky="e")
        self.personas_var = tk.IntVar(value=1)
        self.personas_spin = tk.Spinbox(form_frame, from_=1, to=4, textvariable=self.personas_var, width=5)
        self.personas_spin.grid(row=3, column=1)

        #fecha de entrada
        tk.Label(form_frame, text="Fecha entrada (DD-MM-YYYY):").grid(row=4, column=0, sticky="e")
        self.entrada_entry = tk.Entry(form_frame)
        self.entrada_entry.grid(row=4, column=1)

        #cantidad de noches
        tk.Label(form_frame, text="Cantidad noches:").grid(row=5, column=0, sticky="e")
        self.noches_var = tk.IntVar(value=1)
        self.noches_spin = tk.Spinbox(form_frame, from_=1, to=30, textvariable=self.noches_var, width=5)
        self.noches_spin.grid(row=5, column=1)

        #botones
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Agregar", command=self.agregar_reserva).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Editar", command=self.editar_reserva).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_reserva).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Limpiar", command=self.limpiar_form).grid(row=0, column=3, padx=5)

        self.actualizar_tabla()

    def _on_close(self):
        self.ventana.destroy()
        if self.on_close:
            self.on_close()

    def _filtrar_reservas(self, *args):
        filtro = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        for clave, res in self.reservas.items():
            # Convert cliente_id to string for .lower()
            cliente = str(res.get("cliente_id", "")).lower()
            if filtro in cliente or filtro in str(clave).lower():
                entrada_fmt = datetime.strptime(res["entrada"], "%d-%m-%Y").strftime("%d-%m-%Y")
                salida_fmt = datetime.strptime(res["salida"], "%d-%m-%Y").strftime("%d-%m-%Y")
                self.tree.insert("", "end", iid=clave, values=(
                        clave,
                    res.get("cliente_id", ""),
                    res.get("piso", ""),
                    res.get("tipo_habitacion", ""),
                    res.get("personas", ""),
                    res.get("habitacion", ""),
                    entrada_fmt,
                    salida_fmt,
                    res.get("noches", ""),
                ))

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
        self._filtrar_reservas()

    def validar_formulario(self):
        if not self.cliente_var.get():
            error_response("Debe seleccionar un cliente.")
            return False
        if self.piso_var.get() not in ["1", "2", "3"]:
            error_response("Debe seleccionar un piso válido (1, 2 o 3).")
            return False
        if self.tipo_var.get() not in ["Estándar", "Suite"]:
            error_response("Debe seleccionar un tipo de habitación válido.")
            return False
        personas = self.personas_var.get()
        if self.tipo_var.get() == "Estándar" and (personas < 1 or personas > 2):
            error_response("La habitación Estándar admite máximo 2 personas.")
            return False
        if self.tipo_var.get() == "Suite" and (personas < 1 or personas > 4):
            error_response("La Suite admite máximo 4 personas.")
            return False
        try:
            fecha_entrada = datetime.strptime(self.entrada_entry.get(), "%d-%m-%Y")
        except ValueError:
            error_response("El formato de la fecha de entrada debe ser DD-MM-YYYY.")
            return False
        hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if fecha_entrada < hoy:
            error_response("La fecha de entrada no puede ser anterior a hoy.")
            return False
        noches = self.noches_var.get()
        if noches < 1 or noches > 30:
            error_response("La cantidad de noches debe estar entre 1 y 30.")
            return False
        return True

    def generar_habitacion(self, piso, tipo):
        habitaciones_existentes = [
            r["habitacion"] for r in self.reservas.values()
            if r.get("piso") == piso and r.get("tipo_habitacion") == tipo
        ]
        max_habs = 12
        for i in range(1, max_habs + 1):
            hab_num = f"{piso}0{i}"
            if hab_num not in habitaciones_existentes:
                return hab_num
        return None

    def validar_conflicto_reserva(self, hab, entrada, salida, clave_actual=None):
        entrada_dt = datetime.strptime(entrada, "%d-%m-%Y")
        salida_dt = datetime.strptime(salida, "%d-%m-%Y")
        for clave, res in self.reservas.items():
            if clave == clave_actual:
                continue  #ignora la reserva que estamos editando
            if res["habitacion"] == hab:
                res_entrada = datetime.strptime(res["entrada"], "%d-%m-%Y")
                res_salida = datetime.strptime(res["salida"], "%d-%m-%Y")
                #si las fechas se juntan
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

        entrada_dt = datetime.strptime(entrada, "%d-%m-%Y")
        salida_dt = entrada_dt + timedelta(days=noches)
        salida = salida_dt.strftime("%d-%m-%Y")

        habitacion = self.generar_habitacion(piso, tipo)
        if habitacion is None:
            error_response("No hay habitaciones disponibles para el piso y tipo seleccionados.")
            return

        # --- NUEVO: Verifica existencia y disponibilidad real de la habitación ---
        if not habitacion_existe(habitacion):
            return error_response("La habitación seleccionada no existe.")
        if habitacion_esta_ocupada(habitacion, entrada, salida, self.reservas):
            return error_response("La habitación está ocupada en ese rango de fechas.")

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
        set_estado_habitacion(habitacion, "ocupado")
        messagebox.showinfo("Éxito", "Reserva agregada correctamente.")
        self.actualizar_tabla()
        self.limpiar_form()

    def eliminar_reserva(self):
        seleccion = self.tree.selection()
        if not seleccion:
            error_response("Debe seleccionar una reserva para eliminar.")
            return

        clave = seleccion[0]
        reserva = self.reservas.get(clave)
        id_hab = reserva.get("habitacion") if reserva else None

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar la reserva seleccionada?"):
            self.reservas.pop(clave, None)
            guardar_reservas(self.reservas)
            # --- NUEVO: Si no hay más reservas activas para esa habitación, marcar como disponible ---
            if id_hab:
                otras_reservas = [
                    r for k, r in self.reservas.items()
                    if r.get("habitacion") == id_hab
                ]
                if not otras_reservas:
                    set_estado_habitacion(id_hab, "disponible")
            self.actualizar_tabla()
            self.limpiar_form()

    def editar_reserva(self):
        seleccion = self.tree.selection()
        if not seleccion:
            error_response("Debe seleccionar una reserva para editar.")
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

        try:
            entrada_dt = datetime.strptime(entrada, "%d-%m-%Y")
        except ValueError:
            error_response("El formato de la fecha de entrada debe ser DD-MM-YYYY.")
            return
        salida_dt = entrada_dt + timedelta(days=noches)
        salida = salida_dt.strftime("%d-%m-%Y")

        habitacion = self.reservas[clave]["habitacion"]  # mantengo habitación asignada

        # --- NUEVO: Verifica existencia y disponibilidad real de la habitación ---
        if not habitacion_existe(habitacion):
            return error_response("La habitación seleccionada no existe.")
        if habitacion_esta_ocupada(habitacion, entrada, salida, self.reservas, clave_actual=clave):
            return error_response("La habitación está ocupada en ese rango de fechas.")

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
        set_estado_habitacion(habitacion, "ocupado")
        messagebox.showinfo("Éxito", "Reserva editada correctamente.")
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
        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_form)