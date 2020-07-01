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
    SteelDoubleChannel = 5
    SteelTube = 5
    SteelPipe = 6
    FilledSteelTube = 7
    FilledSteelPipe = 8
    ICoverPlate = 9
    Joist = 10
    SteelPlate = 11
    SteelRod = 12
    SteelCastellated = 13
    SteelCellular = 14

    ConcreteRectangular = 15
    ConcreteCircle = 16
    ConcreteEncasementRectangle = 17
    ConcreteEncasementCircle = 18
    ConcretePrecastI = 19
    ConcreteTee = 20
    ConcreteL = 21
    ConcreteCross = 22
    ConcreteBox = 23
    ConcretePipe = 24

    ColdFormedC = 25
    ColdFormedZ = 26
    ColdFormedHat = 27

    BucklingRestrainedBrace = 28
    General = 29
    NonePrismatic = 30


class SectionProperties:
    def __init__(self, area: float, as2: float, as3: float, i33: float, i22: float, s33pos: float,
                 s33neg: float, s22pos: float, s22neg: float, r33: float, r22: float, z33: float, z22: float,
                 j: float, cw: float, cg_offset_3dir: float, cg_offset_2dir: float, pna_offset_3dir: float,
                 pna_offset_2dir: float, sc_offset_3dir: float, sc_offset_2dir: float):
        self.Area = area
        self.As2 = as2
        self.As3 = as3
        self.I33 = i33
        self.I22 = i22
        self.S33Pos = s33pos
        self.S33Neg = s33neg
        self.S22Pos = s22pos
        self.S22Neg = s22neg
        self.R33 = r33
        self.R22 = r22
        self.Z33 = z33
        self.Z22 = z22
        self.J = j
        self.Cw = cw
        self.CGOffset3Dir = cg_offset_3dir
        self.CGOffset2Dir = cg_offset_2dir
        self.PNAOffset3Dir = pna_offset_3dir
        self.PNAOffset2Dir = pna_offset_2dir
        self.SCOffset3Dir = sc_offset_3dir
        self.SCOffset2Dir = sc_offset_2dir


class SectionModifiers:
    def __init__(self, area: float, shear_area2: float, shear_area3: float, torsional_constant:  float,
                 i22: float, i33: float, mass: float, weight: float):
        self.Area = area
        self.ShearArea2 = shear_area2
        self.ShearArea3 = shear_area3
        self.TorsionalConstant = torsional_constant
        self.I22 = i22
        self.I33 = i33
        self.Mass = mass
        self.Weight = weight


class FrameSection(ABC):
    def __init__(self, name: str, material: StructuralMaterial,
                 section_shape: SectionShape, comment=""):
        self.ID = uuid.uuid1().int
        self.Name = name
        self.Material = material
        self.SectionShape = section_shape
        self.Comment = comment
        self.Dimensions: dict = {}
        self.Properties = None
        self.Modifiers = None
        self.SetProperties(SectionProperties(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
        self.SetModifiers(SectionModifiers(1, 1, 1, 1, 1, 1, 1, 1))

    @abstractmethod
    def SetDimensions(self, *p):
        pass

    def SetProperties(self, properties: SectionProperties):
        self.Properties = properties

    def SetModifiers(self, modifiers: SectionModifiers):
        self.Modifiers = modifiers


class GeneralSection(FrameSection):
    def __init__(self, name: str, material: StructuralMaterial, comment=""):
        super().__init__(name, material, SectionShape.General, comment)
        self.SetDimensions(30, 10)

    def SetDimensions(self, depth: float, width: float):
        self.Dimensions = {
            "Depth", depth,
            "Width", width
        }
