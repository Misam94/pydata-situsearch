from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Result:
    frame_id: int
    score: float  # between 0 and 100

    def __post_init__(self):
        if self.score < 0 or self.score > 100:
            raise ValueError("score must be between 0 and 100")


@dataclass(frozen=True)
class ResultSet:
    results: List[Result]


__all__ = [
    'Result',
    'ResultSet'
]
