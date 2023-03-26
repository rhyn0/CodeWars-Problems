"""Nesting Structure Comparison.

4 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/520446778469526ec0000001
"""
__start_date__ = "2022-07-09"


# Standard Library


def same_structure_as(og: list, other: list) -> bool:
    """Return whether og is the same List structure as other.

    Can nest Lists however, using any type of element

    Args:
        og (List): Original to match based on
        other (List): Does this one match the og

    Returns:
        bool: True if match, False otherwise.
    """
    if type(og) != type(other) or len(og) != len(other):
        return False
    for x_el, y_el in zip(og, other, strict=True):
        x_is_list, y_is_list = isinstance(x_el, list), isinstance(y_el, list)
        if x_is_list and y_is_list:
            return same_structure_as(x_el, y_el)
        if x_is_list or y_is_list:
            return False
    return True


class Notes:
    """Learnings from other solutions.

    - i'm doing two instance checks here, lets collapse that into one.
    - Could make use of chained operators since we like equality here
    - Below is an interesting find from community, I like the use of map()
        and how they were able to find a if/else solution
    """

    def same_structure_as(self, og: list, other: list):  # noqa: D102
        if isinstance(og, list) and isinstance(other, list):
            return len(og) == len(other) and map(self.same_structure_as, og, other)
        return type(og) != list != type(other)


if __name__ == "__main__":
    print(same_structure_as([1, 1, 1], [2, 2, 2]))  # True
