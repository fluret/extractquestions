# Your code here
def compute_word_frequency(sentence):
    words = sentence.split()

    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[0])

    for word, frequency in sorted_word_frequency:
        print(f"{word}: {frequency}")


input_sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
compute_word_frequency(input_sentence)
### test.py
import pytest, io, sys, json, mock, re, os

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The solution should return the expected output')
def test_convert_inputs(capsys, app):

    fake_input = ["New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1\n"