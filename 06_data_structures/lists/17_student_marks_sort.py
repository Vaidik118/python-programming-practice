students = [["Aman", 75], ["Riya", 92], ["John", 85], ["Sneha", 90]]

list1 = []

for x in students:
    y = x[1]
    list1.append(y)
    list1.sort()
    list1.reverse()

print(list1)