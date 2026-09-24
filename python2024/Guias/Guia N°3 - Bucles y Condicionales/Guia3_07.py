#7
def factorial (n):
    if n == 0:
        r = 1
    elif n>=1:
        r = n*factorial(n-1)
    return r
n = int(input("Ingrese un numero: "))
print(f"El factorial de {str(n)} es {factorial(n)}")