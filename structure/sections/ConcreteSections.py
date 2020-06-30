from structure.sections.framesection import FrameSection, SectionShape
from structure.material import ConcreteMaterial, RebarMaterial
from structure.sections.ConcreteReinforcement import Reinforcement


class ConcreteRectangularSection(FrameSection):
    def __init__(self, name: str, material: ConcreteMaterial, comment=""):
        super().__init__(name, material, SectionShape.ConcreteRectangular, comment)
        self.Rebars: Reinforcement = None

    def SetReinforcement(self, reinforcement: Reinforcement):
        self.Rebars = reinforcement

    def SetDimensions(self, depth: float, width: float):
        self.Dimensions = {
            "Depth": depth,
            "Width": width
        }

    def SetProperties(self, area, as2, as3, i33, i22, s33pos, s33neg,
                      s22pos, s22neg, r33, r22, z33, z22, j):
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
            "J": j
        }

    def CalcProperties(self):
        pass

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
