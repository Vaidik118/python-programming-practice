def greet(name: str, message: str = "Welcome") -> str:

    return f"{message}, {name}!"


def calculate_bill(price: float, quantity: int = 1, discount: float = 0) -> float:

    if price < 0 or quantity < 0 or discount < 0:
        raise ValueError("Values must be non-negative.")

    total = price * quantity
    return total - discount


def main() -> None:

    print(greet("Vaidik"))

    print(greet("Vaidik", "Hello"))

    print(calculate_bill(100, 3, 20))

    print(calculate_bill(price=100, quantity=3, discount=20))

    print(calculate_bill(500))


if __name__ == "__main__":
    main()