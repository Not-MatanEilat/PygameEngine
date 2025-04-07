from pathlib import Path

import pygame

from engine.colors import WHITE, RED, GREEN, BLUE
from engine.timer.timer import Timer
from engine.ui.button.button import Button
from engine.ui.image.image import Image
from engine.ui.image.image_builder import ImageBuilder
from engine.ui.shapes.circle import Circle
from engine.ui.shapes.circle_surface import CircleSurface
from engine.ui.shapes.rectangle_surface import RectangleSurface
from engine.ui.shapes.triangle import Triangle
from engine.ui.shapes.triangle_surface import TriangleSurface
from engine.ui.text.text_builder import TextBuilder
from engine.window import Window


def main():
    screen = pygame.display.set_mode((1200, 800))

    window = Window(screen=screen, caption="test", background_color=WHITE)
    window.init()
    pygame.font.init()

    text = TextBuilder(pygame.Rect(25, 25, 250, 100)).set_text("messi").create_text()

    button = Button(rect=pygame.Rect(25, 25, 250, 100), text=text, background_color=RED)

    button.set_on_click_listener(lambda:
                                 Timer(lambda: print("yo sir"), 1)
                                 .start())

    rect_surface = RectangleSurface(pygame.Rect(225, 25, 250, 100), RED)
    triangle_surface = TriangleSurface(Triangle(255, 30, 450, 300, 222, 300), GREEN)
    circle_surface = CircleSurface(Circle(255, 445, 35), BLUE)

    image = ImageBuilder(pygame.Rect(50, 50, 250, 250)).create_image()

    image.set_on_click_listener(lambda:
                                Timer(lambda: print("yo sir"), 1)
                                .start())

    running = True
    while running:
        window.screen.fill(window.background_color)

        image.draw(screen)
        # for loop through the event queue
        events = pygame.event.get()
        image.on_event_tick(events)
        for event in events:

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == "__main__":
    main()
