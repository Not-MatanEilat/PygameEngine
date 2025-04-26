from dataclasses import dataclass
from pathlib import Path

from pygame import Surface


@dataclass
class Image:
    path: Path
    # unfortunately, we'll have a coupling to pygame here because converting an image from its pygame format
    # to an other one and then back when not needed is just too much calculations
    image_surface: Surface