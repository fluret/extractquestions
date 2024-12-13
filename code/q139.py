items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
result = [(index, item) for index, item in enumerate(items)]
print(result)

items=["hi", 4, 8.99, 'apple', ('t,b','n')]
result=[n for n in enumerate(items)]
print(result)

mylist = ["hi", 4, 8.99, "apple", ("t,b","n")]
result = [(tuple([index, mylist[index]])) for index in range(len(mylist))]
print(result)



strr=["hi", 4, 8.99, 'apple', ('t,b','n')]  
l=[(strr.index(x),x) for x in strr] 
print(l)
