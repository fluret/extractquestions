def apply_discount(x, y):
    original_price = x
    discount_percentage = y
    total = original_price - (original_price * discount_percentage)
    return f"${total}"


print(apply_discount(10, 0.2))
