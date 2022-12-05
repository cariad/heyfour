from pytest import mark

from heyfour.size import Millimeters
from heyfour.standards.a_series import ASeries, LargeASeries, SmallASeries


@mark.parametrize(
    "t, expect",
    [
        ("2A0", Millimeters(1189, 1682)),
        ("4A0", Millimeters(1682, 2378)),
    ],
)
def test_large__size(t: str, expect: Millimeters) -> None:
    assert LargeASeries().size(t) == expect


@mark.parametrize(
    "t, expect",
    [
        ("A0", Millimeters(841, 1189)),
        ("a0", Millimeters(841, 1189)),
        ("a1", Millimeters(594, 841)),
        ("a2", Millimeters(420, 594)),
        ("a3", Millimeters(297, 420)),
        ("a4", Millimeters(210, 297)),
        ("a5", Millimeters(148, 210)),
        ("a6", Millimeters(105, 148)),
        ("a7", Millimeters(74, 105)),
        ("a8", Millimeters(52, 74)),
        ("a9", Millimeters(37, 52)),
        ("a10", Millimeters(26, 37)),
    ],
)
def test_small__size(t: str, expect: Millimeters) -> None:
    assert SmallASeries().size(t) == expect


@mark.parametrize(
    "t, expect",
    [
        ("a4", Millimeters(210, 297)),
        ("4A0", Millimeters(1682, 2378)),
    ],
)
def test_a_series__size(t: str, expect: Millimeters) -> None:
    assert ASeries().size(t) == expect
