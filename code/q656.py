list_of_dicts = [{"a": 1, "b": 2}, {"b": 2, "c": 3}, {"c": 3, "d": 4}]
dict_set = {frozenset(d.items()) for d in list_of_dicts}
print(list_of_dicts)
print(dict_set)