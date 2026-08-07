# GST using lambda
gst = lambda price : price + (0.18 * price)

# Using list store prices
prices = [100,250,400,1200,50]
prices_with_gst = list(map(gst,prices))

# Print prices and prices with GST
print("Original Prices :",prices)
print("Prices after GST",prices_with_gst)