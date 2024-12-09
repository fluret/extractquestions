s = list(input())

dict_count_ = {k: s.count(k) for k in s}
list_of_tuples = [(k, v) for k, v in dict_count_.items()]
list_of_tuples.sort(key=lambda x: x[1], reverse=True)

for item in list_of_tuples:
    print(item[0], item[1])
