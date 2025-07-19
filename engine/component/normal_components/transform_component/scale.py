from dataclasses import dataclass

@dataclass
class Scale:
    x: float = 0
    y: float = 0

    def __add__(self, other: 'Scale') -> 'Scale':
        return Scale(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: 'Scale') -> 'Scale':
        return Scale(x=self.x - other.x, y=self.y - other.y)