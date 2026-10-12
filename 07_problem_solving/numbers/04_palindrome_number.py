no = int(input("Enter the no:"))
rev = 0
cno = no

while no > 0:
    t = no % 10
    rev = rev * 10 + t
    no = no // 10

if rev == cno:
    print("Yes,number is palindrome")
else:
    print("No,number is not palindrome")