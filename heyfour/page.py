from __future__ import annotations

from heyfour.size import Inches, Millimeters
from heyfour.standards import size_of


class Page:
    """
    Page.
    """

    def __init__(self, size: Inches | Millimeters) -> None:
        self._size = size

    @property
    def inches(self) -> Inches:
        """
        Size in inches.
        """

        if isinstance(self._size, Inches):
            return self._size

        return self._size.inches

    @property
    def millimeters(self) -> Millimeters:
        """
        Size in millimetres.
        """

        if isinstance(self._size, Millimeters):
            return self._size

        return self._size.millimeters


def page_of(size: str | Inches | Millimeters) -> Page:
    """
    Creates a page.

    `size` can be an explicit `Size` or a size code (e.g. "A4").
    """

    if isinstance(size, str):
        size = size_of(size)

    return Page(size)
