# print list of prices
prices = [100,250,400,1200,50,2000,850]

# Prices greater than 500
expensive = list(filter(lambda x : x > 500,prices))

# Prices less than 500
cheap = list(filter(lambda x : x < 500,prices))

# Print both Expensive and Cheap prices
print("Prices Greater than 500",expensive)
print("Prices less than 500",cheap)