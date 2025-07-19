from overrides import override

from engine.collision.collision_checker import CollisionChecker
from engine.colors import Color, darken_color
from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick
from engine.globals.global_manager import GlobalManager
from engine.logger.logger import EngineLogger


class ButtonRendererComponent(BaseComponent):
    def __init__(self, color: Color, border_color: Color):
        super().__init__()

        self._color = color
        self._border_color = border_color

        self._transform_component: TransformComponent = None

    @override
    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    @override
    def on_tick(self, event_tick: EventTick) -> None:

        EngineLogger.debug(f"Transform {self._transform_component.transform.position.x}")
        rect_color = self._color
        if CollisionChecker.rect_collides_point(self._transform_component.transform, event_tick.mouse_events.position) and event_tick.mouse_events.left_click.is_down:
            rect_color = darken_color(self._color)

        GlobalManager.get_instance().get_canvas_manager().draw_rectangle(self._transform_component.transform, rect_color, layer=self.get_layer())
        GlobalManager.get_instance().get_canvas_manager().draw_rectangle_border(self._transform_component.transform, self._border_color, 5, layer=self.get_layer())