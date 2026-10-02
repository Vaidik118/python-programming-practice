total = 100


def local_example() -> None:
    total = 50
    print("Inside function:", total)


def read_global() -> None:
    print("Global value:", total)


def modify_global() -> None:
    global total
    total += 25


def main() -> None:
    print("Before function:", total)

    local_example()
    print("After local function:", total)

    read_global()

    modify_global()
    print("After global modification:", total)


if __name__ == "__main__":
    main()