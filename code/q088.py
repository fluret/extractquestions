def total_cost(d, c, n):
    total_cents = (d * 100 + c) * n
    total_dollars = total_cents // 100
    remaining_cents = total_cents % 100
    return total_dollars, remaining_cents


print(total_cost(15, 22, 4))
