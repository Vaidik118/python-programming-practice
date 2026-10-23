from math import isqrt


def is_perfect(number: int) -> bool:
    """Return True if number is a perfect number."""

    if number <= 1:
        return False

    # Every integer greater than 1 has 1 as a proper divisor.
    divisor_sum = 1

    # Check divisors only up to the square root.
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            divisor_sum += divisor

            # Find the corresponding divisor.
            paired_divisor = number // divisor

            # Avoid counting a square root twice.
            if paired_divisor != divisor:
                divisor_sum += paired_divisor

            # The sum cannot decrease, so we can stop early.
            if divisor_sum > number:
                return False

    return divisor_sum == number


def main() -> None:
    try:
        number = int(input("Enter a positive integer: "))

        if number <= 0:
            print("Please enter a positive integer.")
        elif is_perfect(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()