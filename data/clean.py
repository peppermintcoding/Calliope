"""Functions for cleaning the dataset"""
import re


def filter_data(text: str) -> str:
    """Filters out weird things from the data"""
    patterns = [
        # pattern for more than 5 _ in a row
        re.compile("_{5,}"),
        # pattern for '.       .       .       .       .'
        re.compile("\.\s{1,}\."),
        # pattern for +++++++++++++
        re.compile("\+{5,}"),
        # pattern for "        ."
        re.compile("\s{3,}\."),
        # pattern for "t t t t t t t t t t t t t t"
        re.compile("t\s{3,}"),
        # pattern for digit and newline
        re.compile("\d\n"),
        # pattern for digit with . and newline
        re.compile("\d\.\n"),
        re.compile("Chorus:\n"),
        re.compile("\xe2\x80\xa2"),
        re.compile("\xe2\x80\x94"),
        re.compile(
            "\*\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0"
        ),
        re.compile(
            "\*\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \*\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 *"
        ),
        re.compile("\*\xc2\xa0\xc2\xa0\xc2\xa0 \*\xc2\xa0\xc2\xa0\xc2\xa0 \*"),
        re.compile("\xe2\x9d\x96"),
        re.compile("Refrain:\n"),
        re.compile("\xc3\x9ea"),
        re.compile("\xe2\x9d\x8f"),
        re.compile("\xe2\x98\xbd"),
    ]
    for pat in patterns:
        text = pat.sub("", text)

    text = re.compile("&amp;").sub("and", text)

    return text
