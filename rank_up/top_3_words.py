"""Most Frequently used words in a Text.

4 Kyu Kata Training from CodeWars
Try this out at: https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
"""
__start_date__ = "2022-07-29"

# Standard Library
from collections import Counter
from string import ascii_lowercase
from string import punctuation


def top_3_words(text: str, common_count: int = 3) -> list[str]:
    """Given a text return a list of 3 most common words in descending order.

    Words are defined as sequences of ascii letters with optional
    interweaving apostrophes (').
    Other characters are deemed whitespace.

    Args:
        text (str): Input text to find most common strings
        common_count (int): N most common results to return

    Returns:
        list[str]: list of N most common words in the given text
    """
    non_apo_punc, text = punctuation.replace("'", ""), text.lower()
    for punc in non_apo_punc:
        text = text.replace(punc, " ")
    word_dict = Counter()
    for word in text.split(" "):
        if any(ch in ascii_lowercase for ch in word):
            word_dict[word] += 1
    return [x[0] for x in word_dict.most_common(common_count)]


class Notes:
    """Learnings from other solutions.

    - I wasn't wrong about using regex originally. Just forgot that
        punctuation equals whitespace.
    - to make sure a string isn't only ``'`` characters, w != "'" * len(w)
    """

    ...


if __name__ == "__main__":
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
    # ['e', 'ddd', 'aa']
    print(top_3_words("ovptkn pvsg ovptkn;_???drfce adt adt"))
    # ['ovptkn', 'adt', 'pvsg']
