def add_numbers(first: int, second: int) -> int:

    return first + second


def multiply_numbers(first: int, second: int) -> int:

    return first * second


def describe_person(name: str, age: int) -> str:

    return f"{name} is {age} years old."


def main() -> None:

    print(add_numbers(10, 20))


    print(add_numbers(first=10, second=20))


    print(describe_person("Vaidik", age=23))


if __name__ == "__main__":
    main()