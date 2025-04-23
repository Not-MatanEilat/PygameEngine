import pygame

from engine.colors import RED, WHITE
from engine.screen.base_screen import BaseScreen, check_quit


class TestScreen(BaseScreen):
    def __init__(self, display_screen: pygame.Surface):
        self._running = True
        self._display_screen = display_screen
        self._text = TextComponentBuilder(pygame.Rect(125, 125, 250, 120)). \
            set_text("test screen"). \
            create_text()
        self._text.set_on_click_listener(lambda: self.finish())

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


    def finish(self) -> None:
        self._running = False