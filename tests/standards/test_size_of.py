from pytest import mark, raises

from heyfour import size_of
from heyfour.size import Millimeters


@mark.parametrize(
    "t, expect",
    [
        ("a3", Millimeters(297, 420)),
        ("2A0", Millimeters(1189, 1682)),
    ],
)
def test(t: str, expect: Millimeters) -> None:
    assert size_of(t) == expect


def test__unrecognised() -> None:
    with raises(ValueError) as ex:
        _ = size_of("foo")

    assert str(ex.value) == "Unrecognised paper size 'foo'"
