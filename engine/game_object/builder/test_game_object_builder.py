from engine.component.test_component import TestComponent
from engine.component.transform_component import TransformComponent
from engine.game_object.game_object import GameObject


class TestGameObjectBuilder():
    @staticmethod
    def create() -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponent())
        game_object.add_component(TestComponent())

        return game_object