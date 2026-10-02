def word_frequency(text: str) -> dict[str, int]:

    words = text.lower().split()

    frequency: dict[str, int] = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def main() -> None:
    text = input("Enter a sentence: ")

    result = word_frequency(text)

    for word, count in result.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()