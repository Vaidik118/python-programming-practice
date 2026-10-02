# Set Problem Solving

# Problem 1: Remove duplicates
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)

# Problem 2: Find common elements
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = set(list1) & set(list2)

print("Common:", common)


# Problem 3: Find elements unique to each list
only_list1 = set(list1) - set(list2)
only_list2 = set(list2) - set(list1)

print("Only in list1:", only_list1)
print("Only in list2:", only_list2)


# Problem 4: Check whether all required values exist
available_skills = {"Python", "SQL", "Django", "Git"}
required_skills = {"Python", "SQL"}

has_all_skills = required_skills.issubset(available_skills)

print("All required skills available:", has_all_skills)