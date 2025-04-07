from pathlib import Path
from typing import Optional

import pygame

from engine.ui.image.image import Image


class ImageNotLoadedError(Exception):
    ...


class ImageBuilder:
    def __init__(self, rect: pygame.Rect):
        self._rect = rect
        self._image: Optional[pygame.Surface] = None

    def load_image(self, image_path: Path) -> 'ImageBuilder':
        image = pygame.image.load(image_path)
        self._image = pygame.transform.scale(image, (self._rect.width, self._rect.height))
        return self

    def create_image(self) -> Image:
        if not self._image:
            raise ImageNotLoadedError("Cannot create an image, no image surface was loaded!")

        return Image(
            rect=self._rect,
            image=self._image
        )

