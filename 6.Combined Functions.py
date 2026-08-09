# Using Filter and map function accordingly
def process_prices(prices):
    discounted_prices = list(map(lambda x : x * 0.9,prices))
    filtered_prices = list(filter(lambda x : x > 300,discounted_prices))
    return discounted_prices,filtered_prices

# Printing list of discounted prices and filtered prices
discounted,filtered = process_prices([100,500,900,50,750,600])
print("Discounted Prices",discounted)
print("Filtered Prices",filtered)
    