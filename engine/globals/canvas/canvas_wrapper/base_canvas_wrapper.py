from abc import ABC, abstractmethod

from engine.colors import Color
from engine.component.image_renderer_component.image import Image
from engine.component.transform_component.position import Position
from engine.component.transform_component.transform import Transform


class BaseCanvasWrapper(ABC):

    @abstractmethod
    def fill(self, color: Color) -> None:
        ...
    @abstractmethod
    def draw_image(self, image: Image, transform: Transform) -> None:
        ...

    @abstractmethod
    def draw_rectangle(self, transform: Transform, color: Color) -> None:
        ...

