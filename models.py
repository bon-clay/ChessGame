from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class ChessFigures(Enum):
    pass


@dataclass
class GameState:
    field: tuple[tuple[int]]


@dataclass
class Place:
    position: tuple[int, int]
