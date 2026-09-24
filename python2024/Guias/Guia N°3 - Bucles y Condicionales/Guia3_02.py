#2
a = 500
b = 456
s = 0
while a != 800:
    s += a
    s += b
    a += 10
    b -= 2
s += 800
print(s)