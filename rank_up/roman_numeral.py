"""Roman Numeral from CodeWars.

4 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/51b66044bce5799a7f000003
"""
__start_date__ = "2022-07-01"


class RomanNumerals:
    """Class for converting between Roman and decimal numbers, both ways."""

    rom_int = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "IX": 9,
        "L": 50,
        "XL": 40,
        "X": 10,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    @staticmethod
    def to_roman(num: int) -> str:
        """Given int, return equivalent roman Numeral.

        Args:
            num (int): int to convert

        Returns:
            str: roman numeral equivalent
        """
        roman_str = ""
        for char, val in RomanNumerals.rom_int.items():
            while num >= val:
                roman_str += char
                num -= val
        return roman_str

    @staticmethod
    def from_roman(rom_num: str) -> int:
        """Given roman numeral, convert to equivalent int.

        Args:
            rom_num (str): Roman numeral

        Returns:
            int: Decimal number
        """
        ret_val, start_ind = 0, 0
        for char, val in RomanNumerals.rom_int.items():
            c_size = len(char)
            while (
                start_ind < len(rom_num)
                and rom_num[start_ind : start_ind + c_size] == char
            ):
                ret_val += val
                start_ind += c_size
        return ret_val

    @staticmethod
    def from_roman2(rom_num: str) -> int:
        """Simpler version of from_roman."""
        ret_val = 0
        for char in reversed(rom_num):
            num = RomanNumerals.rom_int[char]
            if 4 * num < ret_val:
                # only possible after going from higher value char, V -> I
                ret_val -= num
            else:
                ret_val += num
        return ret_val

    """
    Learnings from other solutions:
        -
    """


if __name__ == "__main__":
    ...
