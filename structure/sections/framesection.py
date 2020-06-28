from enum import Enum
import uuid
import sys
from abc import ABC, abstractmethod
sys.path.insert(0, '..')
from material import StructuralMaterial, MaterialType, SteelMaterial


class SectionShape(Enum):
    SteelIFlange = 0
    SteelChannel = 1
    SteelTee = 2
    SteelAngle = 3
    SteelDoubleAngle = 4
    SteelTube = 5
    SteelPipe = 6


class FrameSection(ABC):
    def __init__(self, name: str,
                 material: StructuralMaterial,
                 sectionshape: SectionShape, comment=""):
        self.ID = uuid.uuid1().int
        self.Name = name
        self.Material = material
        self.SectionShape = sectionshape
        self.Comment = comment
        self.Dimensions: dict(str, float) = {}
        self.Properties: dict(str, float) = {}
        self.Modifiers: dict(str, float) = {}

    @abstractmethod
    def SetDimensions(self):
        pass

    @abstractmethod
    def SetProperties(self):
        pass

    @abstractmethod
    def SetModifiers(self):
        pass


class SteelIFlangeSection(FrameSection):
    def __init__(self, name: str, material: SteelMaterial, comment=""):
        super().__init__(name, material, SectionShape.SteelIFlange, comment)

    def SetDimensions(self, outsideheight, topflangewidth, topflangethickness,
                     webthickness, bottomflangewidth, bottomfangethickness):
        pass

    def SetProperties(self):
        pass

    def SetModifiers(self):
        pass


steel = SteelMaterial("steel", 2400, 3600, 2400, 3600)
section = SteelIFlangeSection('a', steel)
print("OK")
