from pytest import mark, raises

from heyfour import Size, size_of


@mark.parametrize(
    "t, expect",
    [
        ("a3", Size(297, 420)),
        ("2A0", Size(1189, 1682)),
    ],
)
def test(t: str, expect: Size) -> None:
    assert size_of(t) == expect


def test__unrecognised() -> None:
    with raises(ValueError) as ex:
        _ = size_of("foo")

    assert str(ex.value) == "Unrecognised paper size 'foo'"
