from heyfour.size import Size
from heyfour.standards.a_series import ASeries

standards = [
    ASeries(),
]


def size_of(code: str) -> Size:
    """
    Gets the size of `code` in portrait-oriented millimetres.

    For example, "A4" returns 210 x 297.
    """

    for handler in standards:
        if size := handler.size(code):
            return size

    raise ValueError(f"Unrecognised paper size '{code}'")
