from pytest import mark

from heyfour import page_of
from heyfour.size import Inches, Millimeters


@mark.parametrize(
    "code, expect",
    [
        ("a4", Inches(8.267716535433072, 11.692913385826772)),
    ],
)
def test_inches(code: str, expect: Inches) -> None:
    assert page_of(code).inches == expect


@mark.parametrize(
    "code, expect",
    [
        ("a4", Millimeters(210, 297)),
    ],
)
def test_millimeters(code: str, expect: Inches) -> None:
    assert page_of(code).millimeters == expect


def test_page_of__size() -> None:
    size = Millimeters(100, 100)
    assert page_of(size).millimeters == size
