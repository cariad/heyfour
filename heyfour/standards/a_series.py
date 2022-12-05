from __future__ import annotations

from re import compile  # pylint: disable=redefined-builtin
from typing import Optional

from heyfour.size import Size
from heyfour.standards.standard import Standard

A0 = Size(841, 1189)


class LargeASeries(Standard):
    """
    Large A-series paper sizes (2A0, 4A0, etc).
    """

    def __init__(self) -> None:
        self._pattern = compile(r"^(\d+)[aA]0$")

    def size(self, code: str) -> Optional[Size]:
        """
        Attempts to translate `code` to a large A-series `Size` in
        portrait-oriented millimetres.
        """

        result = self._pattern.match(code)
        if not result:
            return None

        count = int(result.groups()[0]) // 2

        width = A0.width
        height = A0.height

        for _ in range(count):
            h = width * 2
            width = height
            height = h

        return Size(width, height)


class SmallASeries(Standard):
    """
    Small A-series paper sizes (A0, A1, A2, etc).
    """

    def __init__(self) -> None:
        self._pattern = compile(r"^[aA](\d+)$")

    def size(self, code: str) -> Optional[Size]:
        """
        Attempts to translate `code` to a small A-series `Size` in
        portrait-oriented millimetres.
        """

        result = self._pattern.match(code)
        if not result:
            return None

        count = int(result.groups()[0])

        width = A0.width
        height = A0.height

        for _ in range(count):
            w = height // 2
            height = width
            width = w

        return Size(width, height)


class ASeries(Standard):
    """
    A-series paper sizes (A4, A6, 2A0, etc).
    """

    def __init__(self) -> None:
        self._small = SmallASeries()
        self._large = LargeASeries()

    def size(self, code: str) -> Optional[Size]:
        """
        Attempts to translate `code` to an A-series `Size` in portrait-oriented
        millimetres.
        """

        return self._small.size(code) or self._large.size(code)
