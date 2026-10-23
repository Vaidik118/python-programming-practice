import math

no = int(input("Enter a number: "))

cno = no
f = 0

while no > 0:
    t = no % 10
    f = f + math.factorial(t)
    no = no // 10

if f == cno:
    print(cno, "is a Krishnamurti number")
else:
    print(cno, "is Not a Krishnamurti number")