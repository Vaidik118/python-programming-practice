no = int(input("Enter the no:"))
rev = 0
cno = no

while no > 0:
    t = no % 10
    rev = rev + t * t * t
    no = no // 10

if rev == cno:
    print("Yes,number is Armstrong")
else:
    print("No,number is not Armstrong")