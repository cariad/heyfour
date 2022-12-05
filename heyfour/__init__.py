"""
&copy; 2022 Cariad Eccleston and released under the MIT License.

For usage and support, see https://github.com/cariad/heyfour.
"""

from importlib.resources import files

from heyfour.page import Page, page_of
from heyfour.size import Size
from heyfour.standards import size_of


def version() -> str:
    """
    Gets the package's version.
    """

    with files(__package__).joinpath("VERSION").open("r") as t:
        return t.readline().strip()


__all__ = [
    "Page",
    "Size",
    "page_of",
    "size_of",
    "version",
]
