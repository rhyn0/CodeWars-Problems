# My Modules
from rank_up.roman_numeral import RomanNumerals


def test_roman_to_basic():
    assert RomanNumerals.to_roman(1000) == "M"
    assert RomanNumerals.to_roman(4) == "IV"
    assert RomanNumerals.to_roman(1) == "I"
    assert RomanNumerals.to_roman(1990) == "MCMXC"
    assert RomanNumerals.to_roman(2008) == "MMVIII"


def test_roman_from_basic():
    assert RomanNumerals.from_roman("XXI") == 21
    assert RomanNumerals.from_roman("I") == 1
    assert RomanNumerals.from_roman("IV") == 4
    assert RomanNumerals.from_roman("MMVIII") == 2008
    assert RomanNumerals.from_roman("MDCLXVI") == 1666


def test_roman2_from_basic():
    assert RomanNumerals.from_roman("XXI") == 21
    assert RomanNumerals.from_roman("I") == 1
    assert RomanNumerals.from_roman("IV") == 4
    assert RomanNumerals.from_roman("MMVIII") == 2008
    assert RomanNumerals.from_roman("MDCLXVI") == 1666
