from structure.sections.framesection import FrameSection, SectionShape
from structure.material import SteelMaterial


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


class SteelChannelSection(FrameSection):
    def __init__(self, name: str, material: SteelMaterial, comment=""):
        super().__init__(name, material, SectionShape.SteelChannel, comment)

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
