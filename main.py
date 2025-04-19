from pathlib import Path

import pygame

from engine.colors import WHITE, RED, GREEN, BLUE
from engine.screen.main_menu_screen import MainMenuScreen
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

    pygame.font.init()

    window = Window(start_screen=MainMenuScreen(screen), display=screen, caption="test")
    window.init()

    text = TextBuilder(pygame.Rect(25, 25, 250, 100)).set_text("messi").create_text()

    button = Button(rect=pygame.Rect(25, 25, 250, 100), text=text, background_color=RED)

    button.set_on_click_listener(lambda:
                                 Timer(lambda: print("yo sir"), 1)
                                 .start())
    window.run()

    #
    # rect_surface = RectangleSurface(pygame.Rect(225, 25, 250, 100), RED)
    # triangle_surface = TriangleSurface(Triangle(255, 30, 450, 300, 222, 300), GREEN)
    # circle_surface = CircleSurface(Circle(255, 445, 35), BLUE)
    #
    #
    #
    #
    # running = True
    # while running:
    #     window.display_screen.fill(window.background_color)
    #
    #     # for loop through the event queue
    #     events = pygame.event.get()
    #     triangle_surface.draw(screen)
    #     for event in events:
    #
    #         # Check for QUIT event
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #     pygame.display.flip()


if __name__ == "__main__":
    main()
