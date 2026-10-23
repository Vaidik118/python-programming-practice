def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers."""

    if a == 0 or b == 0:
        return 0

    common_divisor = gcd(a, b)

    # Divide first to reduce the intermediate product.
    return abs((a // common_divisor) * b)


def main() -> None:
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))

        result = lcm(a, b)

        print(f"LCM of {a} and {b} is {result}")

    except ValueError:
        print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()