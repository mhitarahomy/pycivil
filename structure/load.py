'''Define load classes'''
import uuid
from enum import Enum


class LoadCaseType(Enum):
'''Load case types'''
    none = 0
    dead = 1
    live = 2
    seismic = 3
    snow = 4
    soil = 5
    wind = 6
    flood = 7


# Load Case
class LoadCase:
    def __init__(self, name: str, load_case_type: LoadCaseType,
                 comment: str = ""):
        self.ID: int = uuid.uuid1().int
        self.Name: str = name
        self.LoadCaseType: LoadCaseType = load_case_type
        self.Comment: str = comment


# Load
class Load:
    def __init__(self, load_case: LoadCase, *magnitude: float):
        self.ID: int = uuid.uuid1().int
        self.LoadCase: LoadCase = load_case
        self.Magnitude = magnitude


# Point Load
class PointLoad:
    class Force(Load):
        def __init__(self, load_case: LoadCase, fx: float,
                     fy: float, fz: float, mx: float, my: float, mz: float):
            Load.__init__(self, load_case, fx, fy, fz, mx, my, mz)

    class Temprature(Load):
        def __init__(self, load_case: LoadCase, temprature: float):
            Load.__init__(self, load_case, temprature)

    class Displacement(Load):
        def __init__(self, load_case: LoadCase,
                     transx: float, transy: float, transz: float,
                     rotx: float, roty: float, rotz: float):
            Load.__init__(self, load_case, transx, transy, transz,
                          rotx, roty, rotz)


# Linear Load
class LinearLoad:
    class LinearLoadDirection:
        Fx = 0
        Fy = 1
        Fz = 2
        Mx = 3
        My = 4
        Mz = 5

    class Distributed(Load):
        pass


# loadcase = LoadCase("dead load", LoadCaseType.dead)
# load = PointLoad.Temprature(loadcase, 25)
# print(load.LoadCase.Name)
# print(load.ID)
# print(load.Magnitude)
