def triangle_area(base: float, height: float) -> float:
    """Return the area of a triangle."""
    return 0.5 * base * height


def main() -> None:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = triangle_area(base, height)
    print("Area of triangle:", area)


if __name__ == "__main__":
    main()
    