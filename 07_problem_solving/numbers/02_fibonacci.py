n = int(input("enter the number = "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    s = a + b
    a = b
    b = s