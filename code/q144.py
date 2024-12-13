sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'

examine = sentence.split()

result = [word for word in examine if len(word) <4]
print(result)

sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
words=tuple(sentence.split(' '))

result =[i for i in words if len(i) < 4]
print (result)

string = 'all the words in a string'
my_list = [word for word in string.split(' ') if len(word) < 4]
print(my_list)

