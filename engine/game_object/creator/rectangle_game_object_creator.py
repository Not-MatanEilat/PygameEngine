from engine.colors import Color
from engine.component.rectangle_renderer_component.rectangle_renderer_component import RectangleRendererComponent
from engine.component.transform_component.transform_component_builder import TransformComponentBuilder
from engine.game_object.game_object import GameObject


class RectangleGameObjectCreator:
    @staticmethod
    def create(color: Color, layer: int, x: int, y) -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponentBuilder().set_scale(250, 50).set_position(x, y).create_component())
        game_object.add_component(RectangleRendererComponent(color, layer))

        return game_object