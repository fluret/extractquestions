def calculate_tip(x, y):
    bill_total = x
    tip_percentage = y
    tip = bill_total * tip_percentage
    return f"${tip}"


print(calculate_tip(10, 0.15))
