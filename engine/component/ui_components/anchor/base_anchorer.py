from abc import ABC, abstractmethod

from engine.component.transform_component.scale import Scale
from engine.component.transform_component.transform import Transform


class BaseAnchorer(ABC):
    @abstractmethod
    def anchor_transform(self, old_transform_scale: Scale, relative_transform: Transform) -> Transform:
        ...