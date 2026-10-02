def is_palindrome(text: str) -> bool:

    return text == text[::-1]


def main() -> None:
    text = input("Enter a string: ")

    if is_palindrome(text):
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()