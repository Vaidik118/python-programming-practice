stocks = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}


def calculate_average(prices):
    return sum(prices) / len(prices)


def print_stocks(stock_data):
    for name, prices in stock_data.items():
        average = calculate_average(prices)
        print(f"{name} ==> {prices} ==> Average: {average:.2f}")


def add_stock(stock_data, name, price):
    if name in stock_data:
        print(f"{name} already exists.")
        return

    stock_data[name] = [price]
    print(f"{name} added successfully.")


command = input("Enter command (print/add): ").strip().lower()

if command == "print":
    print_stocks(stocks)

elif command == "add":
    name = input("Enter stock name: ").strip().lower()
    price = int(input("Enter price: "))

    add_stock(stocks, name, price)
    print_stocks(stocks)

else:
    print("Invalid command.")