from engine.component.base_component import BaseComponent
from engine.component.test_component import TestComponent


class TransformComponent(BaseComponent):
    def __init__(self):
        super().__init__()

        self.test_component: TestComponent = None

    def start(self) -> None:
        self.test_component = self.get_component(TestComponent)

    def on_tick(self) -> None:
        print(self.test_component.son_of_men_string)