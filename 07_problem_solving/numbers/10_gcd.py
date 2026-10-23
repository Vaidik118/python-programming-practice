def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def main() -> None:
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))

        result = gcd(a, b)

        print(f"GCD of {a} and {b} is {result}")

    except ValueError:
        print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()