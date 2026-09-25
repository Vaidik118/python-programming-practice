hindi = int(input("Enter Hindi marks: "))
english = int(input("Enter English marks: "))
social_science = int(input("Enter Social Science marks: "))

total = hindi + english + social_science


if total < 50:
    grade = "C"
elif total < 100:
    grade = "B"
else:
    grade = "A"

print("Total:", total)
print("Grade:", grade)