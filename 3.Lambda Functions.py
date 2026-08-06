# lambda function gst that returns price after adding the GST of 18% on the price
gst = lambda price: price + (price * 0.18)
print("Price with GST:", gst(100))

# Compute final price after GST and discount together
final_price = lambda price,discount: (price + (0.18 * price)) - discount
print("Final price after discount:", final_price(1000, 100))