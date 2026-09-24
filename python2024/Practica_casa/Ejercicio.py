otro_curso_min = 2.5
otro_curso_max = 7
otro_curso_promedio = 4
curso = 1.5

dif_min = 100 - curso / otro_curso_min * 100
dif_max = 100 - curso / otro_curso_max * 100
dif_promedio = 100 - curso / otro_curso_promedio * 100
print(f"El curso dura un {dif_min}% menos que el rapido")
print(f"El curso dura un {dif_max:.2f}% menos que el lento")
print(f"El curso dura un {dif_promedio}% menos que el promedio")