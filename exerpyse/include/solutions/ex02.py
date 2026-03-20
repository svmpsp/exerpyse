"""Exercise 2: checking palindromes

Complete the function below so that it returns True if
the input word is a palindrome, False otherwise.
"""


def do_things(word: str) -> bool:
    return word == word[::-1]
