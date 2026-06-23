# Stock Portfolio Tracker

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}

def main():
    print(" Welcome to the Stock Portfolio Tracker!")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    portfolio = {}
    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in dictionary. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print(" Please enter a valid number.")

    # Calculate total investment
    total_value = 0
    print("\nYour Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_value += value
        print(f"{stock}: {qty} shares → ${value}")

    print(f"\n Total Investment Value: ${total_value}")

    # Optionally save to file
    save_choice = input("\nDo you want to save the result to a file? (yes/no): ").lower()
    if save_choice == "yes":
        file_type = input("Save as .txt or .csv? ").lower()
        if file_type == "txt":
            with open("portfolio.txt", "w") as f:
                f.write("Portfolio Summary:\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
                f.write(f"\nTotal Investment Value: ${total_value}\n")
            print(" Portfolio saved to portfolio.txt")
        elif file_type == "csv":
            import csv
            with open("portfolio.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Value"])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock] * qty])
                writer.writerow(["Total", "", total_value])
            print(" Portfolio saved to portfolio.csv")
        else:
            print(" Invalid choice. File not saved.")

if __name__ == "__main__":
    main()
