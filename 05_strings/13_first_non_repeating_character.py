def first_non_repeating_character(text: str) -> str | None:

    frequency: dict[str, int] = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    for character in text:
        if frequency[character] == 1:
            return character

    return None


def main() -> None:
    text = input("Enter a string: ")

    result = first_non_repeating_character(text)

    if result is None:
        print("No non-repeating character found.")
    else:
        print("First non-repeating character:", result)


if __name__ == "__main__":
    main()