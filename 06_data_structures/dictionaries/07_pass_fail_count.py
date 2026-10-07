students = {
    "ram": 80,
    "vaidik": 85,
    "parth": 45,
    "kuldip": 35
}

p = 0
f = 0

for key, value in students.items():
    if value > 50:
        print("pass")
        p += 1
    else:
        print("fail")
        f += 1

print("number of pass student=", p)
print("number of fail student=", f)