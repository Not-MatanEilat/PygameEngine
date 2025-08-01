from imaplib import Debug

from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.position import Position
from engine.events.event_tick import EventTick
from engine.events.keyboard_events.key import Key
from engine.globals.global_manager import GlobalManager
from engine.logger.logger import EngineLogger


class CameraMovingComponent(BaseComponent):
    def __init__(self, speed: float):
        super().__init__()
        self._speed = speed


    def start(self) -> None:
        pass

    def on_tick(self, event_tick: EventTick) -> None:
        camera = GlobalManager.get_instance().get_current_screen().get_camera()
        if event_tick.keyboard_events.is_released(Key.LEFT):
            camera.add_to_position(Position(self._speed, 0))

        if event_tick.mouse_events.left_click.is_down:
            camera.add_to_position(Position(-self._speed, 0))