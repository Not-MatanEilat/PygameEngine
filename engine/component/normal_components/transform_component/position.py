from dataclasses import dataclass

@dataclass
class Position:
    x: float = 0
    y: float = 0

    def __add__(self, other: 'Position') -> 'Position':
        return Position(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: 'Position') -> 'Position':
        return Position(x=self.x - other.x, y=self.y - other.y)