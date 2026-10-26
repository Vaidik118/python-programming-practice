list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

r = []

for x in list1:
    if list1.count(x) == 1:
        r.append(x)

print(r)