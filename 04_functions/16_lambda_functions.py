from functools import reduce


def add_regular(a: int, b: int) -> int:
    return a + b


add_lambda = lambda a, b: a + b


def main() -> None:

    print(add_lambda(10, 20))


    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda number: number ** 2, numbers))
    print("Squares:", squares)


    even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
    print("Even numbers:", even_numbers)


    students = [
        ("Amit", 75),
        ("Vaidik", 90),
        ("Rahul", 82),
    ]

    students_sorted = sorted(students, key=lambda student: student[1])
    print("Sorted:", students_sorted)


    total = reduce(lambda x, y: x + y, numbers)
    print("Total:", total)


if __name__ == "__main__":
    main()