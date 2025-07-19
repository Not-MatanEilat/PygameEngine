from engine.component.normal_components.transform_component.transform_builder import TransformBuilder
from engine.component.ui_components.text_component.text_builder import TextBuilder
from engine.component.ui_components.text_component.text_renderer_component import TextRendererComponent
from engine.game_object.game_object import GameObject


class TextGameObjectCreator:
    @staticmethod
    def create(text: str) -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformBuilder().create_component())
        game_object.add_component(TextRendererComponent(TextBuilder().set_text(text).create_text()))

        return game_object
