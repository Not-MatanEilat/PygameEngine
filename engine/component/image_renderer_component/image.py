from dataclasses import dataclass
from pathlib import Path

from pygame import Surface


@dataclass
class Image:
    path: Path
    image_surface: Surface
