from math import isqrt


def is_prime(number: int) -> bool:
    """Return True if number is prime; otherwise return False."""

    if number < 2:
        return False

    # Checking divisors beyond sqrt(number) is unnecessary.
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            return False

    return True


def main() -> None:
    try:
        number = int(input("Enter an integer: "))

        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()