from pytest import raises

from heyfour import Size


def test_init__too_narrow() -> None:
    with raises(ValueError) as ex:
        _ = Size(-1, -2)

    assert str(ex.value) == "Page must be wider than 0; got (-2 x -1)"
