def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def calculate(a: int, b: int) -> dict[str, int]:
    return {
        "addition": add(a, b),
        "subtraction": subtract(a, b),
        "multiplication": multiply(a, b),
    }


def main() -> None:
    result = calculate(10, 5)

    print("Addition:", result["addition"])
    print("Subtraction:", result["subtraction"])
    print("Multiplication:", result["multiplication"])


if __name__ == "__main__":
    main()