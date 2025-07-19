from engine.colors import Color
from engine.component.normal_components.transform_component.transform import Transform
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.component.ui_components.anchor.center_anchorer import CenterAnchorer
from engine.component.ui_components.anchor.right_center_anchorer import RightCenterAnchorer
from engine.component.ui_components.button_renderer_component.button_renderer_component import ButtonRendererComponent
from engine.component.ui_components.click_listener_component.click_listener_component import OnClickCallable, \
    ClickListenerComponent
from engine.component.ui_components.text_component.text_builder import TextBuilder
from engine.component.ui_components.text_component.text_renderer_component import TextRendererComponent
from engine.game_object.game_object import GameObject


class ButtonGameObjectCreator:
    @staticmethod
    def create(transform: Transform, text: str, text_size: float, on_click: OnClickCallable, color: Color, border_color: Color) -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponent(transform))
        game_object.add_component(ClickListenerComponent(on_click))
        game_object.add_component(ButtonRendererComponent(color, border_color))
        game_object.add_component(TextRendererComponent(TextBuilder().set_text(text).set_size(text_size).create_text(), RightCenterAnchorer()))

        return game_object
