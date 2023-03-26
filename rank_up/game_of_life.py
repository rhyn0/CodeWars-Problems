"""Conway's Game of Life from CodeWars.

4 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/52423db9add6f6fc39000354/
"""
__start_date__ = "2022-07-02"
# Standard Library
from copy import deepcopy

moore_neighbors = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

MAX_NEIGHBORS = 3
MIN_NEIGHBOR = 2


def is_in_bounds(local_cells: list[list[int]], row: int, col: int) -> bool:
    """Return True if point (i, j) is in proper bound of the board."""
    return 0 <= row < len(local_cells) and 0 <= col < len(local_cells[row])


def num_neighbors(local_cells: list[list[int]], row: int, col: int) -> int:
    """Return number of live Moore neighbor cells for a given (i, j)."""
    return sum(
        is_in_bounds(local_cells, row + x_mod, col + y_mod)
        and local_cells[row + x_mod][col + y_mod]
        for x_mod, y_mod in moore_neighbors
    )


def add_padding(
    local_cells: list[list[int]],
):
    """Expand the board by 1 cell in all 4 cardinal directions."""
    for i in range(len(local_cells)):
        local_cells[i].insert(0, 0)
        local_cells[i].append(0)
    local_cells.insert(0, [0] * len(local_cells[0]))
    local_cells.append([0] * len(local_cells[0]))


def crop(cells: list[list[int]]):
    """Trim size of board down to contain as little dead cells."""
    top_cut, left_cut, right_cut, bot_cut = float("inf"), float("inf"), 0, 0

    for i, row in enumerate(cells):
        if any(row):
            top_cut = min(i, top_cut)
            bot_cut = max(bot_cut, i)
        for col, val in enumerate(cells[i]):
            if val:
                left_cut = min(col, left_cut)
                right_cut = max(right_cut, col)
    return [row[left_cut : right_cut + 1] for row in cells[top_cut : bot_cut + 1]]


def next_gen(cells):
    """Calculate next generation of cells."""
    add_padding(cells)
    new_cells = []
    for i in range(len(cells)):
        new_cell = []
        for col, val in enumerate(cells[i]):
            neighbors = num_neighbors(cells, i, col)
            if neighbors < MIN_NEIGHBOR or neighbors > MAX_NEIGHBORS:
                new_cell.append(0)
            elif val == 0 and neighbors == MAX_NEIGHBORS:
                new_cell.append(1)
            else:
                new_cell.append(val)
        new_cells.append(new_cell)
    return new_cells


def get_generation(cells: list[list[int]], n: int) -> list[list[int]]:  # given code
    """Driver function for life."""
    local_cells = deepcopy(cells)
    for _ in range(n):
        local_cells = next_gen(local_cells)

    return local_cells


class Notes:
    """Learnings from other solutions.

    - Should I have applied EAFTAP for the get value? Instead of defining
        a bounding function, just return 0 if its out of bounds.
    - Why is my add padding modifying the list in place?
        Can skip the deepcopy use if I use list slicing to return a new array
        rather than using append/insert
    - Since this becomes my copy, just delete the entries from the row 'del'
    - Arguable whethere these should be local bound methods or make them public
        + Well complexity is getting hit with local methods, so making public
    """


if __name__ == "__main__":
    print(get_generation([[1, 0, 0], [0, 1, 1], [1, 1, 0]], 1))
    # [0, 1, 0], [0, 0, 1], [1, 1, 1]
