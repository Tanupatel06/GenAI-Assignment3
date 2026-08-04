# Apply discount on price with default discount percent as 5% and max discount percent as 60%
def apply_discount(price,discount_percent=5):
    if discount_percent > 60:
        discount_percent = 60
    final_price = price - (price*discount_percent/100)
    return final_price

# Getting the price after applying discount
print("Price after 10% Discount:",apply_discount(1000,10))
print("Price with default Discount:",apply_discount(500))
print("price with 70% discount(max 60% allowed)",apply_discount(2000,70))

