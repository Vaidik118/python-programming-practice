def countdown(number: int) -> None:
    if number < 0:
        return

    print(number)

    if number > 0:
        countdown(number - 1)


def main() -> None:
    countdown(5)


if __name__ == "__main__":
    main()