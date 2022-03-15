from enum import Enum
from typing import List


class StringEnum(str, Enum):
    @classmethod
    def values(cls) -> List[str]:
        return [frequency.value for frequency in sorted(cls)]


class NivelArea(StringEnum):
    NO_NIVEL="NIVEL_LOCAL",
    NIVEL_LOCAL="NIVEL_LOCAL"
    NIVEL_MUNICIPAL="NIVEL_MUNICIPAL"
    NIVEL_NACIONAL="NIVEL_NACIONAL"
    NIVEL_INTERNACIONAL = "NIVEL_INTERNACIONAL"
