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
