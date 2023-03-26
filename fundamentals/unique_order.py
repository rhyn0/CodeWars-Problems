"""Unique Order from CodeWars.

6 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/54e6533c92449cc251001667
"""
__start_date__ = "2022-06-30"

# Standard Library
from collections.abc import Iterable
import itertools
from typing import TypeVar

T = TypeVar("T")


def unique_in_order(iterable: Iterable[T]) -> list[T]:
    """Given an iterable, return an iterable removing contiguous repeat values.

    Preserves the order of given iterable.

    Args:
        iterable (Iterable[T]): iterable to slim down

    Returns:
        List[T]: Returns list of less items still in order
    """
    last_seen = object()  # choose impossible first value
    ret_list = []
    for item in iterable:
        if item != last_seen:
            ret_list.append(item)
            last_seen = item
    return ret_list


class Notes:
    """Learnings from other solutions.

    - There is an itertools func for this - groupby
    - could get rid of last_seen var for checking the list, seems bad though
    """


def unique_groupby(iterable: Iterable[T]) -> list[T]:  # noqa: D103
    return [k for k, _ in itertools.groupby(iterable)]


if __name__ == "__main__":
    print(unique_in_order(iter(["0"])))
    print(unique_groupby(iter(["0"])))
