from __future__ import annotations

from math import ceil, isclose
from typing import Any, Generic, TypeVar

UnitT = TypeVar("UnitT", bound=float | int)


class Size(Generic[UnitT]):
    """
    Size.

    The width and height will be arranged to guarantee portait orientation.
    """

    def __init__(self, width: UnitT, height: UnitT) -> None:
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

    @property
    def height(self) -> UnitT:
        """
        Height.
        """

        return self._height

    @property
    def width(self) -> UnitT:
        """
        Width.
        """

        return self._width


MILLIMETERS_PER_INCH = 25.4


class Millimeters(Size[int]):
    @property
    def inches(self) -> Inches:
        return Inches(
            self._width / MILLIMETERS_PER_INCH,
            self._height / MILLIMETERS_PER_INCH,
        )


class Inches(Size[float]):
    @property
    def millimeters(self) -> Millimeters:
        return Millimeters(
            ceil(self._width * MILLIMETERS_PER_INCH),
            ceil(self._height * MILLIMETERS_PER_INCH),
        )
