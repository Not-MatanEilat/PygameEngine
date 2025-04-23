from pathlib import Path

import pygame

from engine.colors import WHITE, RED, GREEN, BLUE
from engine.screen.main_menu_screen import MainMenuScreen
from engine.window import Window


def main():
    screen = pygame.display.set_mode((1200, 800))

    pygame.font.init()

    window = Window(start_screen=MainMenuScreen(screen), display=screen, caption="test")
    window.init()

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
