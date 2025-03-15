import pygame
from pygame import Rect

from engine.colors import WHITE, BLACK
from engine.sprite.position import Position
from engine.timer.timer import Timer
from engine.ui.text.text_builder import TextBuilder
from engine.window import Window


def main():
    screen = pygame.display.set_mode((1200, 800))

    window = Window(screen=screen, caption="test", background_color=WHITE)
    window.init()
    pygame.font.init()

    text = TextBuilder(pygame.Rect(25, 25, 250, 100)).set_text("messi").create_text()

    text.set_on_click_listener(lambda: Timer(lambda: print("yo sir"), 1).start())

    running = True
    while running:
        window.screen.fill(window.background_color)

        text.draw(screen)
        # for loop through the event queue
        events = pygame.event.get()
        text.on_event_tick(events)
        for event in events:

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == "__main__":
    main()