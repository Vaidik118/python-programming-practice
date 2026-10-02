list1 = [11, 44, 500]
list2 = [77, 44, 11, 10]

common = []

for element in list1:
    if element in list2:
        common.append(element)

print(common)