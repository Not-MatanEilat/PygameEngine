import pygame

from engine.colors import WHITE, CYAN2, GRAY1, RED, ORANGE
from engine.component.normal_components.camera_moving_component.camera_moving_component import CameraMovingComponent
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.component.test_components.mouse_position_renderer import MousePositionRenderer
from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.rotation import Rotation
from engine.component.normal_components.transform_component.scale import Scale
from engine.component.normal_components.transform_component.transform import Transform
from engine.component.normal_components.transform_component.transform_builder import TransformBuilder
from engine.component.test_components.original_mouse_position_renderer import OriginalMousePositionRenderer
from engine.game_object.creator.moving_circle_game_object_creator import MovingCircleGameObjectCreator
from engine.game_object.creator.moving_rect_game_object_creator import MovingRectGameObjectCreator
from engine.game_object.game_object import GameObject
from engine.game_object.ui_creator.button_game_object_creator import ButtonGameObjectCreator
from engine.globals.canvas.canvas_manager import CanvasManager
from engine.globals.canvas.canvas_relative_transformer import CanvasRelativeTransformer
from engine.globals.canvas.draw_manager.draw_manager import DrawManager
from engine.globals.global_manager import GlobalManager
from engine.screen.screen import Screen
from engine.window import Window


def f():
    pass


def main():
    pygame.init()

    display_info = pygame.display.Info()
    canvas_surface = pygame.display.set_mode((1200, 800))

    game_object = GameObject()
    game_object.add_component(TransformComponent(TransformBuilder().create_component()))
    game_object.add_component(MousePositionRenderer())

    camera_mover_game_object = GameObject()
    camera_mover_game_object.add_component(TransformComponent(TransformBuilder().create_component()))
    camera_mover_game_object.add_component(CameraMovingComponent(5))

    screen = Screen([
        # RectangleGameObjectCreator.create(ORANGE, 0, 25, 0),
        # RectangleGameObjectCreator.create(RED, 4, 50, 25),
        # RectangleGameObjectCreator.create(YELLOW1, 2, 75, 50)
        # ButtonGameObjectCreator.create(Transform(position=Position(0, 0), scale=Scale(600, 400), rotation=Rotation(0)),
        #                                "hello", 25, lambda: print("hello"), WHITE, GRAY1),
        MovingCircleGameObjectCreator.create(Position(50, 50), 0.05, RED),
        MovingRectGameObjectCreator.create(Position(550, 50), -0.05, ORANGE),
        game_object,
        camera_mover_game_object
    ])

    window = Window(caption="test",
                    global_manager=GlobalManager(
                        canvas_manager=CanvasManager(
                            draw_manager=DrawManager(canvas_surface=canvas_surface),
                            default_background_color=CYAN2),
                        starter_screen=screen))
    window.init()

    window.run()


if __name__ == "__main__":
    main()
