from pathlib import Path

import pygame

from engine.colors import WHITE, ORANGE, RED, YELLOW1, GREEN, CYAN2, GRAY1
from engine.component.transform_component.position import Position
from engine.component.transform_component.rotation import Rotation
from engine.component.transform_component.scale import Scale
from engine.component.transform_component.transform import Transform
from engine.component.transform_component.transform_component_builder import TransformComponentBuilder
from engine.game_object.creator.rectangle_game_object_creator import RectangleGameObjectCreator
from engine.game_object.creator.test_game_object_creator import TestGameObjectCreator
from engine.game_object.ui_creator.button_game_object_creator import ButtonGameObjectCreator
from engine.game_object.ui_creator.text_game_object_creator import TextGameObjectCreator
from engine.globals.canvas.canvas_manager import CanvasManager
from engine.globals.canvas.draw_manager.draw_manager import DrawManager
from engine.globals.global_manager import GlobalManager
from engine.screen.screen import Screen
from engine.window import Window


def f():
    pass


def main():
    pygame.init()

    display_info = pygame.display.Info()
    canvas_surface = pygame.display.set_mode((display_info.current_w, display_info.current_h))
    # canvas_surface = pygame.display.set_mode((1200, 800))

    screen = Screen([
        # RectangleGameObjectCreator.create(ORANGE, 0, 25, 0),
        # RectangleGameObjectCreator.create(RED, 4, 50, 25),
        # RectangleGameObjectCreator.create(YELLOW1, 2, 75, 50)
        ButtonGameObjectCreator.create(Transform(position=Position(0, 0), scale=Scale(600, 1000), rotation=Rotation(0)),
                                       "hello", f, WHITE, GRAY1)
    ])

    print(canvas_surface.get_width(), canvas_surface.get_height())

    window = Window(caption="test",
                    global_manager=GlobalManager(
                        canvas_manager=CanvasManager(
                            draw_manager=DrawManager(canvas_surface),
                            default_background_color=CYAN2),
                        starter_screen=screen))
    window.init()

    window.run()


if __name__ == "__main__":
    main()
