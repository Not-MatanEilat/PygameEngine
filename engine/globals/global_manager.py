from __future__ import annotations
from typing import TYPE_CHECKING


from engine.game_object.game_object import GameObject
from engine.globals.canvas.canvas_manager import CanvasManager
from engine.globals.exceptions import GlobalsNotInitiatedException

if TYPE_CHECKING:
    from engine.screen.screen import Screen


class GlobalManager:
    globals_instance = None

    def __init__(self, canvas_manager: CanvasManager, starter_screen: Screen):
        self._canvas_manager = canvas_manager
        self._current_screen = starter_screen

        GlobalManager.globals_instance = self

    @staticmethod
    def is_initiated() -> bool:
        return GlobalManager.globals_instance is not None

    @staticmethod
    def get_instance() -> 'GlobalManager':
        if not GlobalManager.is_initiated():
            raise GlobalsNotInitiatedException("Cannot get globals instance if it wasn't initiated yet!")

        return GlobalManager.globals_instance

    def get_canvas_manager(self) -> CanvasManager:
        return self._canvas_manager

    def get_current_screen(self) -> Screen:
        return self._current_screen

    def start_new_screen(self, screen: Screen, finish_current=False) -> None:
        self._current_screen.start_screen(screen, finish_current)

    def add_game_object(self, game_object: GameObject) -> None:
        self._current_screen.add_game_object(game_object)

    def on_tick(self) -> None:
        self._canvas_manager.on_tick()
