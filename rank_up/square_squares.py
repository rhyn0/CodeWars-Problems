"""Square Squares from CodeWars.

4 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/54eb33e5bc1a25440d000891
"""
__start_date__ = "2022-07-02"
# Standard Library
from math import ceil
from math import sqrt


def decompose(n: int) -> list[int] | None:
    """Return a strictly increasing sequence of numbers to sum to n squared.

    Must be strictly increasing so no duplicate values.
    Valid answers will not include n.

    Args:
        n (int): Number to square then sum up to

    Returns:
        Union[List[int], None]: Strictly increasing sequence of integers,
            or None on no possible answer.
    """

    def decompose_helper(
        square_num: int, tail_recursion: set[int] = set()  # noqa: B006
    ) -> list[int]:
        if square_num == 0:
            if len(tail_recursion) > 1:
                return sorted(tail_recursion)
            return []

        ceiling = ceil(sqrt(square_num)) + 1
        for i in reversed(range(1, ceiling)):
            if i not in tail_recursion:
                differ = square_num - i**2
                if differ < 0:
                    continue
                val = decompose_helper(differ, tail_recursion.union({i}))
                if val:
                    return val
        return []

    poss_answer = decompose_helper(n**2)
    return poss_answer if len(poss_answer) > 1 else None


class Notes:
    """Learnings from other solutions.

    - If you go for the recursion case, make sure to define base cases
        as simple as possible
        + Zero and less than zero are obvious
    - give more power to helper function, auxiliary functions are not bound
        by the spec given
    """

    ...


# below is another contestants code for this problem
def decompose_ref(num):
    """Compute solution with different methodology.

    Used as reference answer.
    """

    def _recurse(s, i):  # not my code
        if s < 0:
            return None
        if s == 0:
            return []
        for j in range(i - 1, 0, -1):  # not my code
            sub = _recurse(s - j**2, j)
            if sub is not None:
                return [*sub, j]
        return None

    return _recurse(num**2, num)


if __name__ == "__main__":
    print(decompose(11))
    print(decompose(1))
    print(decompose(2))
    print(decompose(4))
    print(decompose(5))
