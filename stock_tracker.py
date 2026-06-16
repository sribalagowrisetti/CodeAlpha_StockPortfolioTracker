# Stock prices (hardcoded dictionary)
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        cost = stocks[stock] * quantity

        portfolio[stock] = portfolio.get(stock, 0) + cost
        total_investment += cost
    else:
        print("Stock not found!")

print("\n===== Summary =====")

for stock, cost in portfolio.items():
    print(f"{stock}: ₹{cost}")

print("\nTotal Investment:", total_investment)

# Save output to file
with open("result.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, cost in portfolio.items():
        file.write(f"{stock}: {cost}\n")
    file.write(f"\nTotal Investment: {total_investment}\n")

print("\nResult saved in result.txt")
