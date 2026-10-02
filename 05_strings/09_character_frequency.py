def character_frequency(text: str) -> dict[str, int]:
    """Return the frequency of each character in the text."""
    frequency: dict[str, int] = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    return frequency


def main() -> None:
    text = input("Enter a string: ")

    result = character_frequency(text)

    for character, count in result.items():
        print(f"{character}: {count}")


if __name__ == "__main__":
    main()