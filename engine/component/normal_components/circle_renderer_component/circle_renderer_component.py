from engine.colors import Color
from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick
from engine.globals.global_manager import GlobalManager


class CircleRendererComponent(BaseComponent):
    def __init__(self, radius: float, color: Color):
        super().__init__()

        self._color = color
        self._radius = radius

        self._transform_component: TransformComponent = None

    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    def on_tick(self, event_tick: EventTick) -> None:
        GlobalManager.get_instance().get_canvas_manager().draw_circle(self._transform_component.transform, self._radius, self._color, layer=self.get_layer())