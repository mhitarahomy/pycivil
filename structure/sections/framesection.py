from enum import Enum
import uuid
import sys
from abc import ABC, abstractmethod
from structure.material import StructuralMaterial, MaterialType, SteelMaterial
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
    def __init__(self, name: str,
                 material: StructuralMaterial,
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


class SteelIFlangeSection(FrameSection):
    def __init__(self, name: str, material: SteelMaterial, comment=""):
        super().__init__(name, material, SectionShape.SteelIFlange, comment)

    def SetDimensions(self, outside_height, top_flange_width, top_flange_thickness,
                      web_thickness, bottom_flange_width, bottom_flange_thickness):
        self.Dimensions = {
            "OutSideHeight": outside_height,
            "TopFlangeWidth": top_flange_width,
            "TopFlangeThickness": top_flange_thickness,
            "WebThickness": web_thickness,
            "BottomFlangeWidth": bottom_flange_width,
            "BottomFlangeThickness": bottom_flange_thickness
        }

    def SetProperties(self, area, as2, as3, i33, i22, s33pos, s33neg,
                      s22pos, s22neg, r33, r22, z33, z22, j, cw):
        self.Properties = {
            "Area": area,
            "As2": as2,
            "As3": as3,
            "I33": i33,
            "I22": i22,
            "S33Pos": s33pos,
            "S33Neg": s33neg,
            "S22Pos": s22pos,
            "S22Neg": s22neg,
            "R33": r33,
            "R22": r22,
            "Z33": z33,
            "Z22": z22,
            "J": j,
            "Cw": cw
        }

    def SetModifiers(self, area, shear_area2, shear_area3,
                     torsional_constant, i22, i33, mass, weight):
        self.Modifiers = {
            "Area": area,
            "ShearArea2": shear_area2,
            "ShearArea3": shear_area3,
            "TorsionalConstant": torsional_constant,
            "I22": i22,
            "I33": i33,
            "Mass": mass,
            "Weight": weight
        }


steel = SteelMaterial("steel", 2400, 3600, 2400, 3600)
section = SteelIFlangeSection('a', steel)
print("OK")
