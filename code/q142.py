result = ["even" if n % 2 == 0 else "odd" for n in range(20)]
print(result)

"""
Let's see the for loop and break out the syntax of the list comprehension
"""
result = []
for n in range(20):
    if n % 2 == 0:
        result.append("even")
    else:
        result.append("odd")

"""
List comprehension
[expression for item in list]
expression = "'even' if n %2 == 0 else 'odd'"
for item in list = "for n in range(20)"
"""

[['even','odd'][x%2] for x in numbers]

res = ['odd' if n%2 else 'even' for n in range(20)]