#Lab 2, ejercicio 1
"""Inicializar los precios unitarios de cada fruta y las cantidades en formato de número
entero"""

valor_manzana = 100
valor_pera = 250
valor_durazno = 300

cantidad_manzana = 150
cantidad_pera = 80
cantidad_durazno = 120

#Obtener e imprimir el total a pagar por cada tipo de fruta comprada
print(f"El valor de las manzanas es de ${valor_manzana} y quedan {cantidad_manzana}")
print(f"El valor de las peras es de ${valor_pera} y quedan {cantidad_pera}")
print(f"El valor de los duraznos es de ${valor_durazno} y quedan {cantidad_durazno}")

#a
suma_manzana_pera = valor_manzana + valor_pera
print(suma_manzana_pera)
#b
lista_valor_maximo = [valor_manzana, valor_durazno, valor_pera]
valor_maximo = max(lista_valor_maximo)
print(valor_maximo)
#c
valor_minimo = min(lista_valor_maximo)
print(valor_minimo)

#d
promedio_precio_frutas = (valor_durazno + valor_manzana + valor_pera)/3
print(f"El promedio de todas las frutas juntas es de ${promedio_precio_frutas:.2f}")