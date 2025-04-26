from pathlib import Path

import pygame

from engine.colors import WHITE
from engine.game_object.builder.test_game_object_builder import TestGameObjectBuilder
from engine.globals.canvas.canvas_manager import CanvasManager
from engine.globals.canvas.canvas_wrapper.pygame_canvas_wrapper import PygameCanvasWrapper
from engine.globals.global_manager import GlobalManager
from engine.screen.screen import Screen
from engine.window import Window


def main():
    screen = pygame.display.set_mode((1200, 800))

    pygame.font.init()

    window = Window(caption="test",
                    global_manager=GlobalManager(
                        canvas_manager=CanvasManager(
                            canvas_wrapper=PygameCanvasWrapper(screen),
                            default_background_color=WHITE),
                        starter_screen=Screen([TestGameObjectBuilder.create()])))
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
