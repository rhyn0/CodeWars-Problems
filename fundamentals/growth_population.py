"""Growth Population from CodeWars.

7 Kyu Kata Training from CodeWars

Try this out at: https://www.codewars.com/kata/563b662a59afc2b5120000c6/
"""

__start_date__ = "2022-06-26"


class ExpectedPopulationError(Exception):
    """Error for if initial population value is not-positive."""

    def __init__(self, *args: object) -> None:
        """Default message error."""
        super().__init__("Population values must be greater than 0.", *args)


def nb_year(p0: int, percent: float | int, aug: int, pn: int) -> int:
    """Calculate years to achieve population growth.

    Given intial population p0, growing at percent rate, with an immigration
    flow of aug per year. How long does it take to reach population size of pn?

    Args:
        p0 (int): Initial population
        percent (float): Growth rate as a percent. Input of 2 is 2%
        aug (int): Number of natural immigrants to population
        pn (int): Population to surpass

    Returns:
        int: Number of years to reach the desired population
    """
    if p0 <= 0 or pn <= 0:
        raise ExpectedPopulationError()

    i = 0
    while p0 < pn:
        p0 = int(p0 * (100 + percent) / 100.0 + aug)
        i += 1
    return i


class Notes:
    """Learnings from other solutions.

    - Recursion allows us to skip the i += 1 statement
    - Can simplify the percentage calculation by distributing the / 100.0
    """


if __name__ == "__main__":
    print(nb_year(150000, 0.25, 1000, 2000000))
