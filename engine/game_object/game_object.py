from __future__ import annotations

from typing import List, Type, TYPE_CHECKING, TypeVar

from engine.events.event_tick import EventTick
from engine.game_object.exceptions import DuplicateComponentException, ComponentNotFoundException

if TYPE_CHECKING:
    from engine.component.base_component import BaseComponent

    ComponentType = TypeVar('ComponentType', bound=BaseComponent)



class GameObject:
    def __init__(self, layer=0):
        self.__components: List[BaseComponent] = []
        self.__layer = layer

    def init(self) -> None:
        self.set_game_object_for_components()
        self.start_components()

    def set_game_object_for_components(self) -> None:
        for component in self.__components:
            component.set_game_object(self)

    def start_components(self) -> None:
        for component in self.__components:
            component.start()

    def tick_components(self, event_tick: EventTick) -> None:
        for component in self.__components:
            component.on_tick(event_tick)

    def add_component(self, component: BaseComponent) -> None:
        if is_component_type_in_list(type(component), self.__components):
            raise DuplicateComponentException("Cannot add the same type of component twice!")

        self.__components.append(component)

    def get_layer(self) -> int:
        return self.__layer

    def remove_component(self, component_type: Type[ComponentType]) -> None:
        if not is_component_type_in_list(component_type, self.__components):
            raise ComponentNotFoundException("Did not find the requested component to delete")

        for component in self.__components:
            if isinstance(component, component_type):
                self.__components.remove(component)
                break

    def get_component(self, component_type: Type[ComponentType]) -> ComponentType:
        for component in self.__components:
            if isinstance(component, component_type):
                return component

        raise ComponentNotFoundException("Did not find the requested component to get")

    def has_component(self, component_type: Type[BaseComponent]) -> bool:
        for component in self.__components:
            if isinstance(component, component_type):
                return True

        return False

def is_component_type_in_list(component_type: Type[BaseComponent], list_of_components: List[BaseComponent]) -> bool:
    return any(isinstance(iterating_component, component_type) for iterating_component in list_of_components)
