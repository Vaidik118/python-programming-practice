list1 = [12, 13, 14, 52, 98, 73, 17, 123]
list2 = []

for x in list1:
    list2.append(int(str(x)[::-1]))

print(list2)