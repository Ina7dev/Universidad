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
