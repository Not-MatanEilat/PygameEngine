from engine.component.normal_components.transform_component.transform_builder import TransformBuilder
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.game_object.game_object import GameObject
from engine.screen.camera.camera import Camera


class CameraCreator:
    @staticmethod
    def create_camera() -> Camera:
        camera_game_object = GameObject(name="Camera")
        camera_game_object.add_component(TransformComponent(TransformBuilder().create_component()))

        return Camera(camera_game_object)