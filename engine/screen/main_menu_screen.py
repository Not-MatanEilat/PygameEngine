import pygame

from engine.colors import WHITE
from engine.game_object.builder.test_game_object_builder import TestGameObjectBuilder
from engine.screen.base_screen import BaseScreen, check_quit, start_screen, init_screen


class MainMenuScreen(BaseScreen):
    def __init__(self, display_screen: pygame.Surface):
        super().__init__()

        self._running = True
        self._display_screen = display_screen
        self.add_game_object(TestGameObjectBuilder.create())

    def finish(self) -> None:
        self._running = False

    def run(self) -> None:
        init_screen(self)

        while self._running:
            self._display_screen.fill(WHITE)
            events = pygame.event.get()

            self.tick_game_objects()
            self.event_tick_game_objects(events)

            if check_quit(events):
                self.finish()

            pygame.display.flip()



