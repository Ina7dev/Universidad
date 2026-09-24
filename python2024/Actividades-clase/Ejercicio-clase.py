a= 10

for i in range(1, a + 1):
    for j in range(a - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print(k, end="")
    print()
