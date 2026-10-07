expenses = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190,
    "June": 1980,
    "July": 2400,
    "August": 2250,
    "September": 2100,
    "October": 2400,
    "November": 2150,
    "december": 2500
}


# 1
extra = expenses["February"] - expenses["January"]
print("dollar spand extra compared to January  =", extra)

# 2
total = expenses["January"] + expenses["February"] + expenses["March"]
print("total expenses January to March = ", total)

# 3
for key, value in expenses.items():
    if value == 2400:
        print(key, ": is spent exactly 2400 dollars")

# 4
expenses["june"] = 2080
print(expenses["june"])

# 5
expenses["April"] = expenses["April"] - 200
print("Updated April expense:", expenses["April"])

# 6
for key, value in expenses.items():
    if value == max(expenses.values()):
        print(
            key,
            ": is Highest Expense month and amount =",
            max(expenses.values())
        )

# 8
for key, value in expenses.items():
    if value == min(expenses.values()):
        print(
            key,
            ": is Lowest Expense month and amount =",
            min(expenses.values())
        )