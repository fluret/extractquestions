fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (
    fruit.count("a") + 
    fruit.count("e") + 
    fruit.count("i") + 
    fruit.count("o") + 
    fruit.count("u")) > 2]

print(fruits_with_more_than_two_vowels)