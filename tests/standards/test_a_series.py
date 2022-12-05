from pytest import mark

from heyfour import Size
from heyfour.standards.a_series import ASeries, LargeASeries, SmallASeries


@mark.parametrize(
    "t, expect",
    [
        ("2A0", Size(1189, 1682)),
        ("4A0", Size(1682, 2378)),
    ],
)
def test_large__size(t: str, expect: Size) -> None:
    assert LargeASeries().size(t) == expect


@mark.parametrize(
    "t, expect",
    [
        ("A0", Size(841, 1189)),
        ("a0", Size(841, 1189)),
        ("a1", Size(594, 841)),
        ("a2", Size(420, 594)),
        ("a3", Size(297, 420)),
        ("a4", Size(210, 297)),
        ("a5", Size(148, 210)),
        ("a6", Size(105, 148)),
        ("a7", Size(74, 105)),
        ("a8", Size(52, 74)),
        ("a9", Size(37, 52)),
        ("a10", Size(26, 37)),
    ],
)
def test_small__size(t: str, expect: Size) -> None:
    assert SmallASeries().size(t) == expect


@mark.parametrize(
    "t, expect",
    [
        ("a4", Size(210, 297)),
        ("4A0", Size(1682, 2378)),
    ],
)
def test_a_series__size(t: str, expect: Size) -> None:
    assert ASeries().size(t) == expect
