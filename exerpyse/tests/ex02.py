"""Tests for exercise 2: palindromes"""


def test_palindrome(test_func):
    print("* Your code should check for palindromes")
    try:
        a = "ailatiditalia"
        res = test_func(a)
        expected = True
        assert res == expected
    except AssertionError as err:
        print("TEST FAILED for ex02.py!")
        print(
            f"The string '{a}' is a palidrome. "
            f"Instead, your code returned {res}.\n"
        )
        raise ValueError("test sum failed") from err
