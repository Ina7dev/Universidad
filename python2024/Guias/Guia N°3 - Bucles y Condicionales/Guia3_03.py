#3
td = 12000
tn = 16000

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
tdid = td + 2000
tnod = tn + 3000

# Definir los turnos de trabajo de cada em
ems = {
    "Empleado 1": {
        "Lunes": "Nocturno",
        "Martes": "Nocturno",
        "Miércoles": "Nocturno",
        "Jueves": "Diurno",
        "Viernes": "Diurno",
        "Sábado": "",
        "Domingo": ""
    },
    "Empleado 2": {
        "Lunes": "",
        "Martes": "Nocturno",
        "Miércoles": "Nocturno",
        "Jueves": "Nocturno",
        "Viernes": "",
        "Sábado": "",
        "Domingo": "Diurno"
    },
    "Empleado 3": {
        "Lunes": "",
        "Martes": "",
        "Miércoles": "Diurno",
        "Jueves": "Diurno",
        "Viernes": "Diurno",
        "Sábado": "Nocturno",
        "Domingo": "Nocturno"
    }
}

#Calcular el pago diario y total semanal para cada em
for em, ho in ems.items():
    ps = 0
    for dia, turno in ho.items():
        if turno == "Diurno":
            if dia == "Domingo":
                pd = tdid * 10
            else:
                pd = td * 10
        elif turno == "Nocturno":
            if dia == "Domingo":
                pd = tnod * 10
            else:
                pd = tn * 10
        else:
            pd = 0
        
        if turno != "":
            print(f"{em} trabaja {dia} en turno {turno}: Pago diario = {pd} CLP")
            ps += pd
    
    # Agregar el total semanal al diccionario del em
    ems[em]["Pago_Semanal"] = ps
    print(f"Total semanal de {em}: {ps} CLP\n")

# Imprimir el resultado final
for em, info in ems.items():
    print(f"Empleado: {em}")
    print(f"  Pago semanal total: {info['Pago_Semanal']} CLP\n")