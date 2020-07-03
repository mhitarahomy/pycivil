from structure.sections.FrameSection import FrameSection, SectionShape, SectionDimensions
from structure.material import SteelMaterial


class SteelIFlangeDimensions(SectionDimensions):
    def __init__(self, outside_height: float, top_flange_width: float, top_flange_thickness: float,
                 web_thickness: float, bottom_flange_width: float, bottom_flange_thickness: float,
                 fillet_radius: float):
        super().__init__(max(top_flange_width, bottom_flange_width), outside_height)
        self.OutSideHeight, self.H = outside_height
        self.TopFlangeWidth, self.btop = top_flange_width
        self.TopFlangeThickness, self.ttop = top_flange_thickness
        self.WebThickness, self.tw = web_thickness
        self.WebHeight, self.hw = self.H - self.tbot - self.ttop
        self.BottomFlangeWidth, self.bbot = bottom_flange_width
        self.BottomFlangeThickness, self.tbot = bottom_flange_thickness
        self.FilletRadius, self.r = fillet_radius


class SteelIFlangeSection(FrameSection):
    def __init__(self, name: str, material: SteelMaterial, comment=""):
        super().__init__(name, material, SectionShape.SteelIFlange, comment)
        self.SetDimensions(50, 15, 1, 2, 15, 1)

    def SetDimensions(self, outside_height: float, top_flange_width: float, top_flange_thickness: float,
                      web_thickness: float, bottom_flange_width: float, bottom_flange_thickness: float,
                      fillet_radius: float):
        self.Dimensions = {
            "OutSideHeight": outside_height,
            "TopFlangeWidth": top_flange_width,
            "TopFlangeThickness": top_flange_thickness,
            "WebThickness": web_thickness,
            "BottomFlangeWidth": bottom_flange_width,
            "BottomFlangeThickness": bottom_flange_thickness,
            "FilletRadius": fillet_radius
        }
        self.CalcProperties()

    def CalcProperties(self):
        pass


class SteelChannelSection(FrameSection):

    def __init__(self, name: str, material: SteelMaterial, comment=""):
        super().__init__(name, material, SectionShape.SteelChannel, comment)
        self.SetDimensions(30, 20, 1, 2, 0)

    def SetDimensions(self, total_depth: float, total_width: float, flange_thickness: float,
                      web_thickness, fillet_radius):
        self.Dimensions = {
            "TotalDepth": total_depth,
            "TotalWidth": total_width,
            "FlangeThickness": flange_thickness,
            "WebThickness": web_thickness,
            "FilletRadius": fillet_radius
        }
        self.CalcProperties()

    def CalcProperties(self):
        pass


class SteelTeeSection(FrameSection):
    def __init__(self, name: str, material: SteelMaterial, comment=""):
        super().__init__(name, material, SectionShape.SteelTee, comment)
        self.SetDimensions(30, 20, 1, 2, 0)

    def SetDimensions(self, total_depth: float, total_width: float, flange_thickness: float,
                      web_thickness: float, fillet_radius: float):
        self.Dimensions = {
            "TotalDepth": total_depth,
            "TotalWidth": total_width,
            "FlangeThickness": flange_thickness,
            "WebThickness": web_thickness,
            "FilletRadius": fillet_radius
        }
        self.CalcProperties()

    def CalcProperties(self):
        pass
