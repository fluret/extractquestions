def cumulative_sum(num_list):
    return [sum(num_list[: i + 1]) for i in range(len(num_list))]


print(cumulative_sum([1, 1, 1]))
print(cumulative_sum([1, 2, 3, 4]))
