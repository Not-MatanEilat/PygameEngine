import pygame.mouse
from overrides import override

from engine.collision.collision_checker import CollisionChecker
from engine.colors import Color, darken_color
from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.component.ui_components.text_component.text_builder import TextBuilder
from engine.events.event_tick import EventTick
from engine.globals.global_manager import GlobalManager
from engine.logger.logger import EngineLogger


class OriginalMousePositionRenderer(BaseComponent):
    def __init__(self):
        super().__init__()

        self._transform_component: TransformComponent = None
        self.position_text = TextBuilder().set_size(25).create_text()

    @override
    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    @override
    def on_tick(self, event_tick: EventTick) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.position_text.set_text(f"old: {mouse_x}, {mouse_y}")
        new_transform = self._transform_component.transform.clone()
        new_transform.position.y += 5
        GlobalManager.get_instance().get_canvas_manager().draw_text(self.position_text, new_transform)