from dataclasses import dataclass

@dataclass
class CreationRule:
    regex: str | None = None
    min_int: int | None = None
    max_int: int | None = None
    min_float: float | None = None
    max_float: float | None = None