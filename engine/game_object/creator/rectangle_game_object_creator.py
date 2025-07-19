from engine.colors import Color
from engine.component.normal_components.rectangle_renderer_component.rectangle_renderer_component import RectangleRendererComponent
from engine.component.normal_components.transform_component.transform_builder import TransformBuilder
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.game_object.game_object import GameObject


class RectangleGameObjectCreator:
    @staticmethod
    def create(color: Color, layer: int, x: int, y) -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponent(TransformBuilder().set_scale(250, 50).set_position(x, y).create_component()))
        game_object.add_component(RectangleRendererComponent(color, layer))

        return game_object