"""Functions for cleaning the dataset"""
import re


def filter_data(text: str) -> str:
    """Filters out weird things from the data"""
    patterns = [
        # pattern for more than 5 _ in a row
        re.compile(b"_{5,}"),
        # pattern for '.       .       .       .       .'
        re.compile(b"\.\s{1,}\."),
        # pattern for +++++++++++++
        re.compile(b"\+{5,}"),
        # pattern for "        ."
        re.compile(b"\s{3,}\."),
        # pattern for "t t t t t t t t t t t t t t"
        re.compile(b"t\s{3,}"),
        # pattern for digit and newline
        re.compile(b"\d\n"),
        # pattern for digit with . and newline
        re.compile(b"\d\.\n"),
        re.compile(b"Chorus:\n"),
        re.compile(b"\xe2\x80\xa2"),
        re.compile(b"\xe2\x80\x94"),
        re.compile(
            b"\*\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0"
        ),
        re.compile(
            b"\*\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \*\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 *"
        ),
        re.compile(b"\*\xc2\xa0\xc2\xa0\xc2\xa0 \*\xc2\xa0\xc2\xa0\xc2\xa0 \*"),
        re.compile(b"\xe2\x9d\x96"),
        re.compile(b"Refrain:\n"),
        re.compile(b"\xc3\x9ea"),
        re.compile(b"\xe2\x9d\x8f"),
        re.compile(b"\xe2\x98\xbd"),
    ]
    for pat in patterns:
        text = pat.sub(b"", text)

    text = re.compile(b"&amp;").sub(b"and", text)

    return text
