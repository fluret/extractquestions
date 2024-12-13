list1 = ["abc", "def", "ghi"]
list2 = ["jkl", "mno", "pqr"]
char_pos_sum_dict = {(x, y): sum(ord(char) for char in x) + sum(ord(char) for char in y) for x in list1 for y in list2}
print(list1)
print(list2)
print(char_pos_sum_dict)