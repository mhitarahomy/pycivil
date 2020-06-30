from enum import Enum
from structure.material import RebarMaterial


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
