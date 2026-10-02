def show_profile(**details: str) -> None:

    for key, value in details.items():
        print(f"{key}: {value}")


def create_student(**student_data: str) -> dict[str, str]:

    return student_data


def main() -> None:
    show_profile(
        name="Vaidik",
        role="Python Developer",
        city="Ahmedabad",
    )

    student = create_student(
        name="Vaidik",
        course="Python",
        level="Intermediate",
    )

    print(student)


if __name__ == "__main__":
    main()