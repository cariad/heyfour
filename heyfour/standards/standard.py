from abc import ABC, abstractmethod
from typing import Optional

from heyfour.size import Millimeters


class Standard(ABC):
    """
    Base class for page size standards.
    """

    @abstractmethod
    def size(self, code: str) -> Optional[Millimeters]:
        """
        Attempts to translate `code` to a `Size` in portrait-oriented
        millimetres.
        """
