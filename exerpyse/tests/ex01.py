"""Tests for exercise 1: summing two numbers"""
import random


def test_sum(test_func):
    print("* Summing two numbers should return their sum")
    try:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        res = test_func(a, b)
        expected = a + b
        assert res == expected
    except AssertionError as err:
        print(f"TEST FAILED for ex01.py!")
        print(
            f"The sum of {a} and {b} should be {expected}. Instead, your code returned {res}.\n"
        )
        raise ValueError(f"test sum failed") from err


def test_commutative(test_func):
    print("* Sum has the commutative property")
    try:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        res = test_func(a, b)
        expected = test_func(b, a)
        assert res == expected
    except AssertionError as err:
        print(f"TEST FAILED for ex01.py!")
        print(
            f"The sum of {a} and {b} should be {expected}. Instead, your code returned {res}.\n"
        )
        raise ValueError(f"test sum failed") from err
