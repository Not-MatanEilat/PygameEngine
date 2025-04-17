import pygame

from engine.colors import WHITE
from engine.screen.base_screen import BaseScreen, check_quit, start_screen
from engine.screen.test_screen import TestScreen
from engine.ui.text.text_builder import TextBuilder


class MainMenuScreen(BaseScreen):
    def __init__(self, display_screen: pygame.Surface):
        self._running = True
        self._display_screen = display_screen
        self._text = TextBuilder(pygame.Rect(125, 125, 250, 120)). \
            set_text("main menu screen"). \
            create_text()
        self._text.set_on_click_listener(lambda: start_screen(self, TestScreen(self._display_screen), finish_current=True))

    def finish(self) -> None:
        self._running = False

    def run(self) -> None:
        while self._running:
            self._display_screen.fill(WHITE)
            events = pygame.event.get()

            self._text.draw(self._display_screen)
            self._text.on_event_tick(events)
            self._text.on_tick()

            if check_quit(events):
                self.finish()

            pygame.display.flip()



