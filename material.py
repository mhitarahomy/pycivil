from enum import Enum
import random
class GeneralMaterial:
    def __init__(self, name: str, density: float, comment=""):
        self.id: str = str(random.randint(1,9))
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
        ConcreteMaterial.name: str = "C20"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 245440
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 200
        return cls

    @classmethod
    def C21(cls):
        ConcreteMaterial.name: str = "C21"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 249570
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 210
        return cls

    @classmethod
    def C23(cls):
        ConcreteMaterial.name: str = "C23"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 257540
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 230
        return cls

    @classmethod
    def C25(cls):
        ConcreteMaterial.name: str = "C25"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 265180
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 250
        return cls

    @classmethod
    def C28(cls):
        ConcreteMaterial.name: str = "C28"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 276080
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 280
        return cls

    @classmethod
    def C30(cls):
        ConcreteMaterial.name: str = "C30"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 283020
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 300
        return cls

    @classmethod
    def C35(cls):
        ConcreteMaterial.name: str = "C35"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 299430
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 350
        return cls

    @classmethod
    def C40(cls):
        ConcreteMaterial.name: str = "C40"
        ConcreteMaterial.Type: MaterialType = MaterialType.Concrete
        ConcreteMaterial.density: float = 2500
        ConcreteMaterial.E: float = 314710
        ConcreteMaterial.nu: float = 0.15
        ConcreteMaterial.A: float = 0.00001
        ConcreteMaterial.fc: float = 400
        return cls

c30 = ConcreteMaterial.C30();
print(c30.E)
print(c30.fc)
