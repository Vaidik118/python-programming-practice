def demonstrate_slicing(text: str) -> None:
    """Demonstrate common string slicing operations."""
    print("Original :", text)
    print("First 5  :", text[:5])
    print("From 5   :", text[5:])
    print("Middle   :", text[2:7])
    print("Step 2   :", text[::2])
    print("Reverse  :", text[::-1])


def main() -> None:
    text = "Python Programming"

    demonstrate_slicing(text)


if __name__ == "__main__":
    main()