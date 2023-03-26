# Standard Library
from collections import Counter
import re
import string

# External Party
from hypothesis import given
from hypothesis import strategies as st

# My Modules
from rank_up.top_3_words import top_3_words


def words_solution(txt: str) -> list[str]:
    return [
        fs[0]
        for fs in Counter(
            w for w in re.findall(r"[a-z']+", txt.lower()) if w != "'" * len(w)
        ).most_common(3)
    ]


def test_top_words_basic():
    TESTS = (
        "a a a  b  c c  d d d d  e e e e e",
        "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e",
        "  //wont won't won't ",
        "  , e   .. ",
        "  ...  ",
        "  '  ",
        "  '''  ",
        """In a village of La Mancha, the name of which I have no desire to cao
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income.""",
        "a a a  b  c c X",
        "a a c b b",
    )
    for tst in TESTS:
        assert top_3_words(tst) == words_solution(tst)


@given(st.text([c for c in string.ascii_lowercase + string.punctuation]))
def test_top_words_random(in_str: str):
    assert top_3_words(in_str) == words_solution(in_str)
