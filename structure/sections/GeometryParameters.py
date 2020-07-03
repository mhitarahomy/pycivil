import math
from typing import Tuple


class Rectangular:
    @staticmethod
    def Area(length: float, width: float) -> float:
        return length * width

    @staticmethod
    def ElasticCenter(b: float, h: float) -> Tuple[float, float]:
        return b/2, h/2

    @staticmethod
    def PlasticCenter(b: float, h: float) -> Tuple[float, float]:
        return b/2, h/2

    @staticmethod
    def MomentOfInertia(b: float, h: float) -> Tuple[float, float]:
        return (b * math.pow(h, 3))/12, (h * math.pow(b, 3))/12

    @staticmethod
    def ElasticSectionModulus(b: float, h: float) -> Tuple[float, float]:
        return (b * math.pow(h, 2)) / 6, (h * math.pow(b, 2)) / 6

    @staticmethod
    def PlasticSectionModulus(b: float, h: float) -> Tuple[float, float]:
        return (b * math.pow(h, 2)) / 4, (h * math.pow(b, 2)) / 4

    @staticmethod
    def RadiusOfGyration(b: float, h: float) -> Tuple[float, float]:
        Ix, Iy = Rectangular.MomentOfInertia(b, h)
        A = Rectangular.Area(b, h)
        return math.sqrt(Ix / A), math.sqrt(Iy / A)


print(Rectangular.ElasticSectionModulus(1, 1))
