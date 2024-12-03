"""Test suite for the exercises."""

from .ex01 import test_commutative, test_sum
from .ex02 import test_palindrome

TEST_SUITE = {
    "ex01.py": [test_sum, test_commutative],
    "ex02.py": [test_palindrome],
}
