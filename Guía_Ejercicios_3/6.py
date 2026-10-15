def resolver_3x3(a, b):
    # a) eliminar x1 de la ecuacion 2 y 3
    m21 = a[1][0] / a[0][0]
    m31 = a[2][0] / a[0][0]

    a22 = a[1][1] - m21 * a[0][1]
    a23 = a[1][2] - m21 * a[0][2]
    b2 = b[1] - m21 * b[0]

    a32 = a[2][1] - m31 * a[0][1]
    a33 = a[2][2] - m31 * a[0][2]
    b3 = b[2] - m31 * b[0]

    # b) eliminar x2 de la ecuacion 3
    m32 = a32 / a22
    a33 = a33 - m32 * a23
    b3 = b3 - m32 * b2

    # sustitucion regresiva, de abajo hacia arriba
    x3 = b3 / a33
    x2 = (b2 - a23 * x3) / a22
    x1 = (b[0] - a[0][1] * x2 - a[0][2] * x3) / a[0][0]
    return x1, x2, x3


# d) sistema del ejercicio
a = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

# c) si a11 es cero se intercambia con una fila que no lo tenga en cero
if a[0][0] == 0:
    for i in range(1, 3):
        if a[i][0] != 0:
            a[0], a[i] = a[i], a[0]
            b[0], b[i] = b[i], b[0]
            break

x1, x2, x3 = resolver_3x3(a, b)
print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)