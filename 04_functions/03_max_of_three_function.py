def max3():
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    no3 = int(input("Enter no3: "))

    if no1 == no2 == no3:
        print("All three numbers are equal")

    elif no1 == no2 and no1 > no3:
        print("no1 and no2 are maximum and equal")

    elif no1 == no3 and no1 > no2:
        print("no1 and no3 are maximum and equal")

    elif no2 == no3 and no2 > no1:
        print("no2 and no3 are maximum and equal")

    elif no1 > no2 and no1 > no3:
        print("no1 is maximum")

    elif no2 > no1 and no2 > no3:
        print("no2 is maximum")

    else:
        print("no3 is maximum")


max3()