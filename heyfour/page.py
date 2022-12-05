from __future__ import annotations

from heyfour.size import Size
from heyfour.standards import size_of


class Page:
    """
    Page.
    """

    def __init__(self, size_millimeters: Size) -> None:
        self._mm = size_millimeters

    @property
    def inches(self) -> Size:
        """
        Size in inches.
        """

        return self._mm / 25.4

    @property
    def millimeters(self) -> Size:
        """
        Size in millimetres.
        """

        return self._mm


def page_of(size: str | Size) -> Page:
    """
    Creates a page.

    `size` can be an explicit `Size` or a size code (e.g. "A4").
    """

    if isinstance(size, str):
        size = size_of(size)

    return Page(size)
