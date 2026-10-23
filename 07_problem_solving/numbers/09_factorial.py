def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""

    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def main() -> None:
    try:
        number = int(input("Enter a non-negative integer: "))

        result = factorial(number)

        print(f"Factorial of {number} is {result}")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()