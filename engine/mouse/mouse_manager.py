from engine.component.transform_component.position import Position
from engine.mouse.mouse_wrapper import BaseMouseWrapper
from engine.mouse.pygame_mouse_wrapper import PygameMouseWrapper


class MouseManager:
    mouse_wrapper: BaseMouseWrapper = PygameMouseWrapper()

    @staticmethod
    def get_mouse_position() -> Position:
        return MouseManager.mouse_wrapper.get_mouse_position()