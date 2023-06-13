import pytest

from .main import check_text


@pytest.mark.parametrize(
    "text, expected",
    [
        ("ыдвшоаыолвтас", False),
        ("ля ля ля ля ля", False),
        ("good", False),
        ("123", False),
        ("👍", True),
        ("Все ок", True),
        ("было челенджево, но суперски. респект", True),
        ("👍", True),
        ("", False),
        ("было лтдтттдтдлб, но суперски. лфрапорфп", False),
    ],
)
def test_check_text(text, expected):
    assert check_text(text) == expected
