from enum import Enum
import random


class GeneralMaterial:
    def __init__(self, name: str, density: float, comment=""):
        self.id: str = str(random.randint(1, 9))
        self.name: str = name
        self.density: float = density
        self.comment: str = comment


class MaterialType(Enum):
    Steel = 1
    Concrete = 2
    Aluminum = 3
    Rebar = 4
    Tendon = 5
    Masonry = 6


class StructuralMaterial(GeneralMaterial):
    def __init__(self, name: str, material_type: MaterialType, 
                 density: float, modulus_of_elasticity: float, nu: float,
                 coefficient_of_thermal_expansion: float):
        self.Type = material_type
        self.E = modulus_of_elasticity
        self.nu = nu
        self.G = self.E/(2*(1+self.nu))
        self.A = coefficient_of_thermal_expansion
        GeneralMaterial.__init__(self, name, density, "")


class ConcreteMaterial(StructuralMaterial):
    def __init__(self, name: str, density: float,
                 modulus_of_elasticity: float, fc: float):
        self.fc = fc
        StructuralMaterial.__init__(self, name, MaterialType.Concrete,
                                    density, modulus_of_elasticity, 0.15, 0.00001)

    @classmethod
    def C20(cls):
        ConcreteMaterial.name = "C20"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 245440
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 200
        return cls

    @classmethod
    def C21(cls):
        ConcreteMaterial.name = "C21"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 249570
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 210
        return cls

    @classmethod
    def C23(cls):
        ConcreteMaterial.name = "C23"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 257540
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 230
        return cls

    @classmethod
    def C25(cls):
        ConcreteMaterial.name = "C25"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 265180
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 250
        return cls

    @classmethod
    def C28(cls):
        ConcreteMaterial.name = "C28"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 276080
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 280
        return cls

    @classmethod
    def C30(cls):
        ConcreteMaterial.name = "C30"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 283020
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 300
        return cls

    @classmethod
    def C35(cls):
        ConcreteMaterial.name = "C35"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 299430
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 350
        return cls

    @classmethod
    def C40(cls):
        ConcreteMaterial.name = "C40"
        ConcreteMaterial.Type = MaterialType.Concrete
        ConcreteMaterial.density = 2500
        ConcreteMaterial.E = 314710
        ConcreteMaterial.nu = 0.15
        ConcreteMaterial.A = 0.00001
        ConcreteMaterial.fc = 400
        return cls


class SteelMaterial(StructuralMaterial):
    def __init__(self, name: str, fy: float, fu: float, fye: float,
                 fue: float):
        self.Fy: float = fy
        self.Fu: float = fu
        self.Fye: float = fye
        self.Fue: float = fue
        super().__init__(name, MaterialType.Steel, 7849.05,
                         20390000000, 0.3, 0.0000117)

    @classmethod
    def ST37_Rolled(cls):
        SteelMaterial.name = "ST37Rolled"
        SteelMaterial.Type = MaterialType.Steel
        SteelMaterial.density = 7849.05
        SteelMaterial.E = 2000000
        SteelMaterial.nu = 0.3
        SteelMaterial.A = 0.0000117
        SteelMaterial.Fy = 2400
        SteelMaterial.Fu = 3700
        SteelMaterial.Fye = 2400 * 1.2
        SteelMaterial.Fue = 3700 * 1.2
        return cls

    @classmethod
    def ST37_Plate(cls):
        SteelMaterial.name = "ST37Plate"
        SteelMaterial.Type = MaterialType.Steel
        SteelMaterial.density = 7849.05
        SteelMaterial.E = 2000000
        SteelMaterial.nu = 0.3
        SteelMaterial.A = 0.0000117
        SteelMaterial.Fy = 2400
        SteelMaterial.Fu = 3700
        SteelMaterial.Fye = 2400 * 1.15
        SteelMaterial.Fue = 3700 * 1.15
        return cls

    @classmethod
    def ST52_Rolled(cls):
        SteelMaterial.name = "ST52Rolled"
        SteelMaterial.Type = MaterialType.Steel
        SteelMaterial.density = 7849.05
        SteelMaterial.E = 2000000
        SteelMaterial.nu = 0.3
        SteelMaterial.A = 0.0000117
        SteelMaterial.Fy = 3600
        SteelMaterial.Fu = 5200
        SteelMaterial.Fye = 3600 * 1.2
        SteelMaterial.Fue = 5200 * 1.2
        return cls

    @classmethod
    def ST52_Plate(cls):
        SteelMaterial.name = "ST52Plate"
        SteelMaterial.Type = MaterialType.Steel
        SteelMaterial.density = 7849.05
        SteelMaterial.E = 2000000
        SteelMaterial.nu = 0.3
        SteelMaterial.A = 0.0000117
        SteelMaterial.Fy = 3600
        SteelMaterial.Fu = 5200
        SteelMaterial.Fye = 3600 * 1.15
        SteelMaterial.Fue = 5200 * 1.15
        return cls


class RebarMaterial(StructuralMaterial):
    def __init__(self, name: str, fy: float, fu: float):
        self.Fy: float = fy
        self.Fu: float = fu
        super().__init__(name, MaterialType.Rebar, 7849.05,
                         20390000000, 0.3, 0.0000117)

    @classmethod
    def AI(cls):
        RebarMaterial.name = "AI"
        RebarMaterial.Type = MaterialType.Rebar
        RebarMaterial.density = 7849.05
        RebarMaterial.E = 2000000
        RebarMaterial.nu = 0.3
        RebarMaterial.A = 0.0000117
        RebarMaterial.Fy = 2400
        RebarMaterial.Fu = 3600
        return cls

    @classmethod
    def AII(cls):
        RebarMaterial.name = "AII"
        RebarMaterial.Type = MaterialType.Rebar
        RebarMaterial.density = 7849.05
        RebarMaterial.E = 2000000
        RebarMaterial.nu = 0.3
        RebarMaterial.A = 0.0000117
        RebarMaterial.Fy = 3400
        RebarMaterial.Fu = 5000
        return cls

    @classmethod
    def AIII(cls):
        RebarMaterial.name = "AIII"
        RebarMaterial.Type = MaterialType.Rebar
        RebarMaterial.density = 7849.05
        RebarMaterial.E = 2000000
        RebarMaterial.nu = 0.3
        RebarMaterial.A = 0.0000117
        RebarMaterial.Fy = 4000
        RebarMaterial.Fu = 6000
        return cls

    @classmethod
    def AIV(cls):
        RebarMaterial.name = "AIV"
        RebarMaterial.Type = MaterialType.Rebar
        RebarMaterial.density = 7849.05
        RebarMaterial.E = 2000000
        RebarMaterial.nu = 0.3
        RebarMaterial.A = 0.0000117
        RebarMaterial.Fy = 5000
        RebarMaterial.Fu = 6500
        return cls

# st37 = SteelMaterial.ST37_Plate();
# print(st37.E)
# print(st37.Fu)
