#Asignamos el valor de las variables.
mp = 100
pp = 250
dp = 300
#Aasignamos la cantidad unitaria.
mc = 150
pc = 80
dc = 120
#Imprimimos el valor unitario y la cantidad.
print(f"Quedan {int(mc)} manzanas y el valor unitario es de ${int(mp)} CLP")
print(f"Quedan {int(pc)} peras y el valor unitario es de ${int(pp)} CLP")
print(f"Quedan {int(dc)} manzanas y el valor unitario es de ${int(dp)} CLP")
#obtenemos e imprimimos el total a pagar por cada tipo de fruta comprada.
m_pt = mp * mc
p_pt = pp * pc
d_pt = dp * dc
print(f"El valor a pagar por las {int(mc)} unidades de manzana es de {int(m_pt)}")
print(f"El valor a pagar por las {int(pc)} unidades de peras es de {int(p_pt)}")
print(f"El valor a pagar por las {int(dc)} unidades de durazno es de {int(d_pt)}")
#La suma total a pagar por la compra de las manzanas y peras.
mp_t = m_pt + p_pt
print(f"La suma a total a pagar entre las manzanas y las peras es de {int(mp_t)}")
#El valor máximo entre los tres totales utilizando la función correspondiente en Python
l = [m_pt, p_pt, d_pt]
vm = max(l)
print(f"El valor maximo del total entre las 3 frutas es de {int(vm)}")
# El valor mínimo entre los tres totales utilizando la función correspondiente en Python.
mv = min(l)
print(f"El valor minimo del total de las 3 frutas es de {int(mv)}")
#El promedio del precio unitario de todas las frutas.
l1 = [mp, pp, dp]
pu = sum(l1)/3
print(f"El promedio con los valores unitarios de cada fruta es de {pu:.2f}")