from pytest import mark

from heyfour import Size, page_of


@mark.parametrize(
    "code, expect",
    [
        ("a4", Size(8.267716535433072, 11.692913385826772)),
    ],
)
def test_inches(code: str, expect: Size) -> None:
    assert page_of(code).inches == expect


@mark.parametrize(
    "code, expect",
    [
        ("a4", Size(210, 297)),
    ],
)
def test_millimeters(code: str, expect: Size) -> None:
    assert page_of(code).millimeters == expect


def test_page_of__size() -> None:
    size = Size(100, 100)
    assert page_of(size).millimeters == size
