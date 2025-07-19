from dataclasses import dataclass

@dataclass
class Rotation:
    degrees: float = 0

    def __add__(self, other: 'Rotation') -> 'Rotation':
        return Rotation(degrees=self.degrees + other.degrees)

    def __sub__(self, other: 'Rotation') -> 'Rotation':
        return Rotation(degrees=self.degrees - other.degrees)