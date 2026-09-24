d_50 = "Este lápiz solo tiene formato de color azul"
d_50 = d_50[:50]
max = len(d_50) > 50
print(type(max))
d_10 = d_50[:10]


print(f"La descripcion es: {d_50}")
print(f"¿El tamaño de la cadena descripción es mayor a 50 caracteres? {max}")
print(f"Los primeros 10 caracteres de la descripción: {d_10}")