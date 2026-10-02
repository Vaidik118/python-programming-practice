def isprime():
    num = int(input("Enter a number: "))

    if num <= 1:
        print("The number is not prime")
        return

    c = 0

    for i in range(2, num):
        if num % i == 0:
            c = 1
            break

    if c == 0:
        print("The number is prime")
    else:
        print("The number is not prime")


isprime()