import uuid
from typing import List


class Part:
    def __init__(self, name: str, density: float, volume: float):
        self.Name = name
        self.Density = density
        self.Volume = volume
        self.Weight = density * volume


class AssignedPart:
    def __init__(self, part: Part, num: int, coefficient: float):
        self.ID = uuid.uuid1().int
        self.Part = part
        self.Num = num
        self.Coefficient = coefficient


class Component:
    def __init__(self, name: str, parts: List[AssignedPart] = []):
        self.ID = uuid.uuid1().int
        self.Name = name
        self.Parts = parts

    def AddPart(self, part: AssignedPart) -> None:
        self.Parts.append(part)

    def Weight(self) -> float:
        weight = 0
        for part in self.Parts:
            weight += part.Part.Weight * part.Num * part.Coefficient
        return weight


class WallLayer(Part):
    def __init__(self, name: str, density: float, thickness: float):
        super().__init__(name, density, thickness)


class AssignedWallLayer(AssignedPart):
    def __init__(self, layer: WallLayer, num: int, coefficient: float):
        super().__init__(layer, num, coefficient)
        self.WallLayer = self.Part


class Wall(Component):
    def __init__(self, name: str, layers: List[AssignedWallLayer] = []):
        super().__init__(name, layers)
        self.Layers = layers

    def AddLayer(self, layer: AssignedWallLayer) -> None:
        self.AddPart(layer)
        self.Layers = self.Parts

    def SurfaceUnitWeight(self) -> float:
        return super().Weight()


layers = [AssignedWallLayer(WallLayer('1', 2400, 0.01), 1, 1)]
wall = Wall('wall', layers)
print(wall.SurfaceUnitWeight())
