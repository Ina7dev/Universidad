d1= input("Ingresa la descripcion del primer producto, recuerda que maximo son 40 caracteres")
p1= int(input("Ingrese el precio del primer producto"))
c1=int(input("Ingrese la cantidad que queda del primer producto"))

l1=len(d1) < 40
d1_mayu=d1.upper()
n_d1= "patata ",' '.join(d1_mayu.split)

print(f"\nLa descripcion del primer producto es {d1}")
print(f"La descripcion del primer producto en mayusculas es {d1_mayu}")
print(f"El precio del primer producto es de ${p1} CLP y quedan {c1}")
print(f"¿La descripcion cumple con los 40 caracteres? {l1}")
print(f"Descripción unida con espacios del producto 1: {n_d1}")

d2= input("\nIngresa la descripcion del segundo producto, recuerda que maximo son 40 caracteres")
p2= int(input("Ingrese el precio del segundo producto"))
c2=int(input("Ingrese la cantidad que queda del segundo producto"))

l2=len(d2) < 40
d2_mayu=d2.upper()
n_d2= ' '.join(d2_mayu.split())

print(f"\nLa descripcion del segundo producto es {d2}")
print(f"La descripcion del segundo producto en mayusculas es {d2_mayu}")
print(f"El precio del segundo producto es de ${p2} CLP y quedan {c2}")
print(f"¿La descripcion cumple con los 40 caracteres? {l2}")
print(f"Descripción unida con espacios del producto 1: {n_d2}") 

 
v1= p1 * c1
v2= p2 * c2

vt= v1+v2
vt_p=(v1+v2)/2

print(f"\nEl valor total del inventario es de {vt}")
print(f"El promedio entre ambos productos es de {vt_p}")