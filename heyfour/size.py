from __future__ import annotations

from math import isclose
from typing import Any


class Size:
    """
    Size.

    The width and height will be arranged to guarantee portait orientation.
    """

    def __init__(self, width: float, height: float) -> None:
        self._width = min(width, height)
        self._height = max(width, height)

        if self._width <= 0:
            raise ValueError(f"Page must be wider than 0; got ({repr(self)})")

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Size)
            and isclose(self.width, other.width)
            and isclose(self.height, other.height)
        )

    def __repr__(self) -> str:
        return f"{self._width} x {self._height}"

    def __truediv__(self, other: Any) -> Size:
        f = float(other)
        return Size(self._width / f, self._height / f)

    @property
    def height(self) -> float:
        """
        Height.
        """

        return self._height

    @property
    def width(self) -> float:
        """
        Width.
        """

        return self._width
