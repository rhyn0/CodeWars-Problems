"""Playing digits from CodeWars.

6 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/5552101f47fc5178b1000050
"""
__start_date__ = "2022-06-27"


# Standard Library
from functools import reduce
from itertools import count
from operator import add


class ExpectedIntegerError(Exception):
    """Error for if input is not a positive integer."""

    def __init__(self, name: str) -> None:
        """Format error to show variable name."""
        super().__init__(f"Expected argument {name!r} to be a positive integer.")


def dig_pow(n: int, p: int) -> int:  # problem statement
    """Find integer that solves the summation if it exists.

    Let C = {x| x is a digit in n}
    Return the integer of sum(Ci ** (p + i) for i in |C|) / n

    Args:
        n (int): number to raise digits to powers of
        p (int): Starting power to raise digits to

    Returns:
        int: -1 if there is no such integer, otherwise return integer
    """
    if not isinstance(n, int) or n < 0:
        raise ExpectedIntegerError("n")
    if not isinstance(p, int) or p < 0:
        raise ExpectedIntegerError("p")

    p_gen = count(p)
    ret_val = reduce(add, (int(c) ** next(p_gen) for c in str(n))) / n
    if not ret_val.is_integer():
        return -1
    return int(ret_val)


class Notes:
    """Learnings from other solutions.

    - Don't divide by n in that line
        + Can test modulo == 0 and then return appropriately
    - Might be more readable to replace the ** with pow
    - Might be more common to replace itertools.count with enumerate
    """

    ...


if __name__ == "__main__":
    print(dig_pow(89, 1))
