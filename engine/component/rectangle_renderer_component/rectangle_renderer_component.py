from engine.colors import Color
from engine.component.base_component import BaseComponent
from engine.component.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick
from engine.globals.global_manager import GlobalManager


class RectangleRendererComponent(BaseComponent):
    def __init__(self, color: Color, layer: int):
        super().__init__()

        self._color = color
        self._layer = layer

        self._transform_component: TransformComponent = None

    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    def on_tick(self, event_tick: EventTick) -> None:
        GlobalManager.get_instance().get_canvas_manager().draw_rectangle(self._transform_component.transform, self._color, layer=self._layer)