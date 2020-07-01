from structure.sections.framesection import FrameSection, SectionShape
from structure.material import ConcreteMaterial
from structure.sections.ConcreteReinforcement import Reinforcement


class ConcreteRectangularSection(FrameSection):
    def __init__(self, name: str, material: ConcreteMaterial, comment=""):
        super().__init__(name, material, SectionShape.ConcreteRectangular, comment)
        self.SetDimensions(30, 20)
        self.Rebars = None
        # self.SetReinforcement(Reinforcement())

    def SetReinforcement(self, reinforcement: Reinforcement):
        self.Rebars = reinforcement

    def SetDimensions(self, depth: float, width: float):
        self.Dimensions = {
            "Depth": depth,
            "Width": width
        }

    def CalcProperties(self):
        pass
