from engine.component.base_component import BaseComponent
from engine.events.event_tick import EventTick


class ImageComponent(BaseComponent):
    def __init__(self):
        super().__init__()


    def start(self) -> None:
        pass

    def on_tick(self, event_tick: EventTick) -> None:
        pass