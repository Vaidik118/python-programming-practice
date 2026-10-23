def reverse_string(text: str) -> str:
    """Return the string in reverse order."""
    return text[::-1]


def main() -> None:
    text = input("Enter a string: ")

    reversed_text = reverse_string(text)

    print("Original string:", text)
    print("Reversed string:", reversed_text)


if __name__ == "__main__":
    main()