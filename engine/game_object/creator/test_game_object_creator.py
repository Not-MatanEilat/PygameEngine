from engine.component.normal_components.transform_component.transform_component_builder import TransformComponentBuilder
from engine.component.ui_components.click_listener_component.click_listener_component import ClickListenerComponent
from engine.component.ui_components.text_component.text_renderer_component import TextRendererComponent
from engine.component.ui_components.text_component.text_builder import TextBuilder
from engine.game_object.game_object import GameObject
from engine.logger.logger import EngineLogger


class TestGameObjectCreator:
    @staticmethod
    def create() -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponentBuilder().set_scale(250, 50).create_component())
        game_object.add_component(TextRendererComponent(TextBuilder().set_text("test_text").create_text()))
        game_object.add_component(ClickListenerComponent(lambda: EngineLogger.info("clicked")))

        return game_object