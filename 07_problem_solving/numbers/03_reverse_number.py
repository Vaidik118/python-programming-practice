no = int(input("Enter the no:"))
rev = 0
cno = no

while no > 0:
    t = no % 10
    rev = rev * 10 + t
    no = no // 10

print("Number:", cno)
print("reverse number:", rev)