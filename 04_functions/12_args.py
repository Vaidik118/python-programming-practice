def add_numbers(*numbers: int) -> int:

    return sum(numbers)


def find_average(*numbers: float) -> float:

    if not numbers:
        raise ValueError("At least one number is required.")

    return sum(numbers) / len(numbers)


def main() -> None:
    print(add_numbers(10, 20))
    print(add_numbers(10, 20, 30, 40, 50))

    print(find_average(10, 20, 30))
    print(find_average(5, 10, 15, 20))


if __name__ == "__main__":
    main()