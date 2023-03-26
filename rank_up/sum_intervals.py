"""Sum of Intervals from CodeWars.

4 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/52b7ed099cdc285c300001cd
"""
__start_date__ = "2022-07-01"

# Standard Library
from operator import itemgetter


def sum_of_intervals(inters: list[tuple[int, int]]) -> int:
    """Given list of intervals, return range that they cover.

    If two intervals overlap, that range should only be counted once

    Args:
        inters (List[Tuple[int, int]]): List of intervals

    Returns:
        int: Range covered by all intervals
    """

    def is_overlapping_interval(
        inter1: tuple[int, int], inter2: tuple[int, int]
    ) -> bool:
        return inter1[0] <= inter2[0] <= inter1[1]

    sort_inter = sorted(inters, key=itemgetter(0, 1))
    interval_set = set()
    i = 0
    while i < len(sort_inter):
        forward_inter = i + 1
        result_interval = sort_inter[i]
        while forward_inter < len(sort_inter) and is_overlapping_interval(
            result_interval, sort_inter[forward_inter]
        ):
            result_interval = result_interval[0], max(
                result_interval[1], sort_inter[forward_inter][1]
            )
            forward_inter += 1
        i = forward_inter
        interval_set.add(result_interval)
    return sum(y - x for x, y in interval_set)


class Notes:
    """Learnings from other solutions.

    - what we aren't looking for is the mathematical calculation, we just want to
        see the number of integers this range covers. so traverse all of them
    - problem with integer traversal is speed, since O(n*m) where m is
        the avg interval length. not each integer adds to
        the solution either
    """

    ...


def top_bottom_pointers(intervals: list[tuple[int, int]]) -> int:
    """Computes interval range with different method.  # noqa: D401.

    Used for answer checking.
    """
    interval_range, top = 0, float("-inf")
    for start, end in sorted(intervals, key=itemgetter(0, 1)):
        if end <= top:
            continue
        max_in_inter = int(max(start, top))
        interval_range += end - max_in_inter
        top = end
    return interval_range


if __name__ == "__main__":
    print(sum_of_intervals([(0, 1), (-1, 2)]))
    print(top_bottom_pointers([(0, 1), (-1, 2)]))
