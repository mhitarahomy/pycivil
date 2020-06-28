from enum import Enum
import uuid
import sys
sys.path.insert(0, '..')
from material import StructuralMaterial
import material


class SectionShape(Enum):
    SteelIFlange = 0
    SteelChannel = 1
    SteelTee = 2
    SteelAngle = 3
    SteelDoubleAngle = 4
    SteelTube = 5
    SteelPipe = 6


class FrameSection:
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


steel = StructuralMaterial("steel",
                           material.MaterialType.Steel,
                           7850, 2000000, 0.2, 0.00001)
section = FrameSection('a', steel, SectionShape.SteelIFlange)
print(section.Dimensions)
