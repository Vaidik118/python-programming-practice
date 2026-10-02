def demonstrate_string_methods(text: str) -> None:
    """Demonstrate commonly used string methods."""

    print("Original   :", repr(text))
    print("Upper      :", text.upper())
    print("Lower      :", text.lower())
    print("Title      :", text.title())
    print("Capitalize :", text.capitalize())
    print("Strip      :", text.strip())
    print("Replace    :", text.replace("python", "Django"))
    print("Split      :", text.split())
    print("Startswith :", text.startswith("Hello"))
    print("Endswith   :", text.endswith("world"))
    print("Is Alpha   :", text.isalpha())
    print("Is Digit   :", text.isdigit())
    print("Find       :", text.find("python"))


def main() -> None:
    text = "  Hello python world  "

    demonstrate_string_methods(text)


if __name__ == "__main__":
    main()