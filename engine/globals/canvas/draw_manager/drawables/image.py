import os.path
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

import pygame

from engine.globals.canvas.draw_manager.drawables.exceptions import ImagePathNotFoundException


@dataclass
class Image:
    pygame_image: pygame.image
    image_bytes_stream: BytesIO
    image_path: Path

def load_image(image_path: Path) -> Image:
    if not os.path.exists(image_path):
        raise ImagePathNotFoundException(f"Could not find image path: {image_path}")

    with image_path.open("rb") as image_file:
        return Image(image_bytes_stream=BytesIO(image_file.read()),
                     image_path=image_path,
                     pygame_image=pygame.image.load(image_path))