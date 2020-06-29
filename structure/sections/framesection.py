from enum import Enum
import uuid
from abc import ABC, abstractmethod
from structure.material import StructuralMaterial
# sys.path.insert(0, '..')
# from material import StructuralMaterial, MaterialType, SteelMaterial


class SectionShape(Enum):
    SteelIFlange = 0
    SteelChannel = 1
    SteelTee = 2
    SteelAngle = 3
    SteelDoubleAngle = 4
    SteelTube = 5
    SteelPipe = 6


class FrameSection(ABC):
    def __init__(self, name: str, material: StructuralMaterial,
                 section_shape: SectionShape, comment=""):
        self.ID = uuid.uuid1().int
        self.Name = name
        self.Material = material
        self.SectionShape = section_shape
        self.Comment = comment
        self.Dimensions: dict[str, float] = {}
        self.Properties: dict[str, float] = {}
        self.Modifiers: dict[str, float] = {}

    @abstractmethod
    def SetDimensions(self, *p):
        pass

    @abstractmethod
    def SetProperties(self, *p):
        pass

    @abstractmethod
    def SetModifiers(self, *p):
        pass
