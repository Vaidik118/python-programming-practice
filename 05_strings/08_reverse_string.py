def reverse_string(text: str) -> str:

    return text[::-1]


def main() -> None:
    text = input("Enter a string: ")

    print("Reversed:", reverse_string(text))


if __name__ == "__main__":
    main()