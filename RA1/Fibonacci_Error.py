import math

aureo = (1 + math.sqrt(5)) / 2

error_deseado = float(input("Ingresa el porcentaje de error que quieres: "))

a = 1
b = 1
terminos = 2
division = b / a
error = abs(aureo - division) / aureo * 100

# se avanza en la serie hasta que el error sea menor o igual al que se pidio
while error > error_deseado:
    a, b = b, a + b
    terminos += 1
    division = b / a
    error = abs(aureo - division) / aureo * 100
    print(f"{b} / {a} = {division}  error: {error}%")

print(f"Se necesitan {terminos} terminos de la serie")
print(f"Aproximacion: {division}")
print(f"Error porcentual: {error}%")