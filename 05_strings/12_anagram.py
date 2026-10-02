def are_anagrams(first: str, second: str) -> bool:

    return sorted(first) == sorted(second)


def main() -> None:
    first = input("Enter first string: ")
    second = input("Enter second string: ")

    if are_anagrams(first, second):
        print("Anagrams")
    else:
        print("Not anagrams")


if __name__ == "__main__":
    main()