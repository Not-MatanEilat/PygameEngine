from pathlib import Path

import pygame

from engine.colors import WHITE, ORANGE, RED, YELLOW1
from engine.game_object.builder.rectangle_game_object_creator import RectangleGameObjectCreator
from engine.game_object.builder.test_game_object_creator import TestGameObjectCreator
from engine.globals.canvas.canvas_manager import CanvasManager
from engine.globals.canvas.draw_manager import DrawManager
from engine.globals.global_manager import GlobalManager
from engine.screen.screen import Screen
from engine.window import Window


def main():
    canvas_surface = pygame.display.set_mode((1200, 800))

    pygame.init()

    screen = Screen([
        # RectangleGameObjectCreator.create(ORANGE, 0, 25, 0),
        # RectangleGameObjectCreator.create(RED, 4, 50, 25),
        # RectangleGameObjectCreator.create(YELLOW1, 2, 75, 50)
        TestGameObjectCreator.create()
    ])

    window = Window(caption="test",
                    global_manager=GlobalManager(
                        canvas_manager=CanvasManager(
                            draw_manager=DrawManager(canvas_surface),
                            default_background_color=WHITE),
                        starter_screen=screen))
    window.init()

    window.run()


if __name__ == "__main__":
    main()
