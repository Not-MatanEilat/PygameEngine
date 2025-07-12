from engine.colors import RED, Color
from engine.component.rectangle_renderer_component.rectangle_renderer_component import RectangleRendererComponent
from engine.component.transform_component.transform import Transform
from engine.component.transform_component.transform_component import TransformComponent
from engine.component.transform_component.transform_component_builder import TransformComponentBuilder
from engine.component.ui_components.anchor.center_anchorer import CenterAnchorer
from engine.component.ui_components.button_renderer_component.button_renderer_component import ButtonRendererComponent
from engine.component.ui_components.click_listener_component.click_listener_component import OnClickCallable, \
    ClickListenerComponent
from engine.component.ui_components.text_component.text_builder import TextBuilder
from engine.component.ui_components.text_component.text_component import TextComponent
from engine.game_object.game_object import GameObject


class ButtonGameObjectCreator:
    @staticmethod
    def create(transform: Transform, text: str, on_click: OnClickCallable, color: Color, border_color: Color) -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponent(transform))
        game_object.add_component(ClickListenerComponent(on_click))
        game_object.add_component(ButtonRendererComponent(color, border_color))
        game_object.add_component(TextComponent(TextBuilder().set_text(text).create_text(), CenterAnchorer()))

        return game_object
