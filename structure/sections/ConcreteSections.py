from structure.sections.framesection import FrameSection, SectionShape
from structure.material import ConcreteMaterial, RebarMaterial
from enum import Enum


class DesignType(Enum):
    Column = 0
    Beam = 1


class ReinforcementConfiguration(Enum):
    Rectangular = 0
    Circular = 1


class ConfinementBars(Enum):
    Ties = 0
    Spirals = 1


class CheckDesign(Enum):
    ToBeChecked = 0
    ToBeDesigned = 1


class Reinforcement:
    def __init__(self, long_bars_material: RebarMaterial, conf_bars_material: RebarMaterial,
                 design_type: DesignType, reinforcement_config: ReinforcementConfiguration,
                 confinement_bars: ConfinementBars, check_design: CheckDesign):
        self.LongBarsMaterial = long_bars_material
        self.ConfBarsMaterial = conf_bars_material
        self.DesignType = design_type
        self.ReinforcementConfig = reinforcement_config
        self.ConfinementBars = confinement_bars
        self.CheckDesign = check_design


class RectangularReinforcement(Reinforcement):
    def __init__(self, long_bars_material: RebarMaterial, conf_bars_material: RebarMaterial,
                 design_type: DesignType, confinement_bars: ConfinementBars, check_design: CheckDesign,
                 clear_cover_conf_bars: float, num_of_long_bars_3dir: float,
                 num_of_long_bars_2dir: float, long_bar_size: float, corner_bar_size: float,
                 conf_bar_size: float, longitudinal_space_conf_bars: float, num_of_conf_bars_3dir: float,
                 num_of_conf_bars_2dir: float):
        super().__init__(long_bars_material, conf_bars_material, design_type, ReinforcementConfiguration.Rectangular,
                         confinement_bars, check_design)
        self.ClearCoverConfBars = clear_cover_conf_bars
        self.NumOfLongBars3dir = num_of_long_bars_3dir
        self.NumOfLongBars2dir = num_of_long_bars_2dir
        self.LongBarSize = long_bar_size
        self.CornerBarSize = corner_bar_size
        self.ConfBarSize = conf_bar_size
        self.LongitudinalSpaceConfBars = longitudinal_space_conf_bars
        self.NumOfConfBars3dir = num_of_conf_bars_3dir
        self.NumOfConfBars2dir = num_of_conf_bars_2dir


class CircularReinforcement(Reinforcement):
    def __init__(self, long_bars_material: RebarMaterial, conf_bars_material: RebarMaterial,
                 design_type: DesignType, confinement_bars: ConfinementBars, check_design: CheckDesign,
                 clear_cover_conf_bars: float, num_of_long_bars: float,
                 long_bar_size: float, conf_bar_size: float, longitudinal_space_conf_bars: float):
        super().__init__(long_bars_material, conf_bars_material, design_type, ReinforcementConfiguration.Rectangular,
                         confinement_bars, check_design)
        self.ClearCoverConfBars = clear_cover_conf_bars
        self.NumOfLongBars = num_of_long_bars
        self.LongBarSize = long_bar_size
        self.ConfBarSize = conf_bar_size
        self.LongitudinalSpaceConfBars = longitudinal_space_conf_bars


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