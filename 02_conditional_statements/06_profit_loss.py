buy_price = float(input("Enter buying price: "))
sell_price = float(input("Enter selling price: "))

if sell_price > buy_price:
    profit = sell_price - buy_price
    print("Profit:", profit)
elif sell_price < buy_price:
    loss = buy_price - sell_price
    print("Loss:", loss)
else:
    print("No profit, no loss")