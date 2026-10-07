marks = {
    "ram": 33,
    "rahul": 45,
    "manav": 30,
    "jayul": 34,
    "meena": 29,
    "siddhi": 48
}

name = input("Enter key for search:").lower()

if name in marks:
    print("yes,is present")
else:
    print("no,is not present")