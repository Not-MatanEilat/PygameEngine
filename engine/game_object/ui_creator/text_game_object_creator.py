from engine.component.transform_component.transform_component_builder import TransformComponentBuilder
from engine.component.ui_components.text_component.text_builder import TextBuilder
from engine.component.ui_components.text_component.text_component import TextComponent
from engine.game_object.game_object import GameObject


class TextGameObjectCreator:
    @staticmethod
    def create(text: str) -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponentBuilder().create_component())
        game_object.add_component(TextComponent(TextBuilder().set_text(text).create_text()))

        return game_object
