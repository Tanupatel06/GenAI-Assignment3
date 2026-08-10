# Function to add prices to the list
def add_price(prices_list, price):
    prices_list.append(price)
    print("Price added successfully.")

# Function to return average prices
def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)

#Function to return maximum price
def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)


prices = []

while True:
    print("\n----- MENU -----")
    print("1. Add price")
    print("2. Show average price")
    print("3. Show highest price")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices, price)

    elif choice == "2":
        print("Average Price:", get_average_price(prices))

    elif choice == "3":
        print("Highest Price:", get_max_price(prices))

    elif choice.lower() == "q":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")