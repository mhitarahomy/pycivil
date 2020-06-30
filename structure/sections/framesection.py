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


class FrameSection(ABC):
    def __init__(self, name: str, material: StructuralMaterial,
                 section_shape: SectionShape, comment=""):
        self.ID = uuid.uuid1().int
        self.Name = name
        self.Material = material
        self.SectionShape = section_shape
        self.Comment = comment
        self.Dimensions: dict = {}
        self.Properties: dict = {}
        self.Modifiers: dict = {}

    @abstractmethod
    def SetDimensions(self, *p):
        pass

    @abstractmethod
    def SetProperties(self, *p):
        pass

    @abstractmethod
    def CalcProperties(self):
        pass

    @abstractmethod
    def SetModifiers(self, *p):
        pass
