#RETO 5
num = int(input("Ingrese un número al que quiera sacar su serie Fibonacci: "))

a = 0
b = 1

f = [a,b]

while True:
    c = a+b
    if c > num:
         break
    f.append(c)
    a = b
    b = c
print(" ".join(map(str,f)))