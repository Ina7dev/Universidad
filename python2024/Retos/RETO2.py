n= input("Ingresa tu nombre: ")
a1={
    "n": n,
    "a": "programacion",
    "n1_1": 2.5,
    "n2_1": 1.7,
    "n3_1": 7.0
}

a2={
    "n": n,
    "a2": "fisica",
    "n1_2": 3.9,
    "n2_2": 6.8,
    "n3_2": 6.9
}

a3={
    "n": n,
    "a3": "mates",
    "n1_3": 3.5,
    "n2_3": 4.7,
    "n3_3": 3.9
}



pn1={
    n: [(a1["a"], {a1["n1_1"], a1["n2_1"], a1["n3_1"]}, 
              round((a1["n1_1"]*0.30) + (a1["n2_1"]*0.50) + (a1["n3_1"]*0.20),1 ))] , 
}
nt1 = tuple(map(str,pn1[n]))
print(f"{n}, a continuación se mostrara el nombre de la asignatura, sus 3 notas y su ponderación final {", ".join(nt1)}")

pn2={
    n: [(a2["a2"], {a2["n1_2"], a2["n2_2"], a2["n3_2"]}, 
              round((a2["n1_2"]*0.30) + (a2["n2_2"]*0.50) + (a2["n3_2"]*0.20),1 ))],
}
nt2 = tuple(map(str,pn2[n]))
print(f"{n}, a continuación se mostrara el nombre de la asignatura, sus 3 notas y su ponderación final {", ".join(nt2)}")
pn3={
    n: [(a3["a3"], {a3["n1_3"], a3["n2_3"], a3["n3_3"]}, 
              round((a3["n1_3"]*0.30) + (a3["n2_3"]*0.50) + (a3["n3_3"]*0.20),1 ))]
}
nt3 = tuple(map(str,pn3[n]))
print(f"{n}, a continuación se mostrara el nombre de la asignatura, sus 3 notas y su ponderación final {", ".join(nt3)}")

