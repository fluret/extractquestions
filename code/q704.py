def is_fibonacci_length(n):
    fib = [0, 1]
    while fib[-1] <= n:
        if fib[-1] == n:
            return True
        fib.append(fib[-1] + fib[-2])
    return False
 
sentence = "Hello, how are you?"
distinct_word_length_fibonacci = {word: len(word) for word in set(sentence.split()) if is_fibonacci_length(len(word))}
print(sentence)
print(distinct_word_length_fibonacci)