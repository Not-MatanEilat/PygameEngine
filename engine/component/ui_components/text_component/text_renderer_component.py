import pygame
from overrides import override

from engine.colors import Color
from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.scale import Scale
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.component.ui_components.anchor.base_anchorer import BaseAnchorer
from engine.component.ui_components.text_component.dynamic_font import DynamicFont
from engine.globals.canvas.draw_manager.drawables.text import Text
from engine.events.event_tick import EventTick
from engine.globals.global_manager import GlobalManager
from engine.logger.logger import EngineLogger


class TextRendererComponent(BaseComponent):
    def __init__(self, text: Text, anchorer: BaseAnchorer):
        super().__init__()
        self._text = text
        self._anchorer = anchorer

        self.transform_component: TransformComponent = None

    @override
    def on_tick(self, event_tick: EventTick) -> None:
        anchored_transform = self._anchorer.anchor_transform(old_transform_scale=Scale(self._text.get_text_surface().get_width(), self._text.get_text_surface().get_height()),
                                                             relative_transform=self.transform_component.transform)
        GlobalManager.get_instance().get_canvas_manager().draw_text(self._text, anchored_transform)

    @override
    def start(self) -> None:
        self.transform_component = self.get_component(TransformComponent)

    def set_text(self, text: str) -> None:
        self._text.set_text(text)

    def get_text(self) -> str:
        return self._text.get_string()

    def set_font(self, font: pygame.Font, size: int) -> None:
        self._text.set_font(font, size)

    def get_font(self) -> DynamicFont:
        return self._text.get_font()

    def set_color(self, color: Color) -> None:
        self._text.set_color(color)

    def get_color(self) -> Color:
        return self._text.get_color()

    def set_size(self, size: int) -> None:
        self._text.set_size(size)

    def set_font_by_name(self, font_name: str) -> None:
        self._text.set_font_by_name(font_name)