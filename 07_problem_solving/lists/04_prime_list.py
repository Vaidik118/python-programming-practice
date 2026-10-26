list1 = [1, 14, 23, 22, 25, 16, 5, 33, 35, 34, 39, 20]
list2 = []

for x in list1:
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            list2.append(x)

print(list2)